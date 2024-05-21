use petgraph::graph::DiGraph;
use std::collections::HashMap;

pub fn page_rank_b(graph: &DiGraph<(), ()>, d: f64, max_iterations: usize, tolerance: f64) -> (Vec<(String, f64)>, usize) {
    let n = graph.node_count();
    let mut p_t = vec![1.0 / n as f64; n];
    let mut adj_matrix = vec![vec![0.0; n]; n];
    let mut iters = 0;

    // Build adjacency matrix
    for node in graph.node_indices() {
        let out_degree = graph.neighbors_directed(node, petgraph::Direction::Outgoing).count();
        if out_degree == 0 {
            continue;
        }
        for neighbor in graph.neighbors_directed(node, petgraph::Direction::Outgoing) {
            adj_matrix[node.index()][neighbor.index()] = 1.0 / out_degree as f64;
        }
    }

    // Build stochastic matrix P
    let mut p_matrix = vec![vec![d / n as f64; n]; n];
    for i in 0..n {
        for j in 0..n {
            p_matrix[i][j] += (1.0 - d) * adj_matrix[i][j];
        }
    }

    // Iteratively calculate p_t+1 = p_t * P
    for _ in 0..max_iterations {
        let mut new_p_t = vec![0.0; n];
        for i in 0..n {
            for j in 0..n {
                new_p_t[i] += p_t[j] * p_matrix[j][i];
            }
        }
        iters += 1;
        // Check for convergence
        let mut diff = 0.0;
        for i in 0..n {
            diff += (new_p_t[i] - p_t[i]).abs();
        }
        if diff < tolerance {
            break;
        }
        p_t = new_p_t;
    }

    // Convert the final p_t vector into a HashMap with node labels
    let mut ranks = HashMap::new();
    for (i, rank) in p_t.iter().enumerate() {
        let label = graph.node_indices()
            .find(|&node| node.index() == i)
            .map(|node| format!("{}", node.index()))
            .unwrap();
        ranks.insert(label, *rank);
    }

    // Sort ranks by values in descending order
    let mut sorted_ranks: Vec<_> = ranks.into_iter().collect();
    sorted_ranks.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());

    (sorted_ranks, iters)
}