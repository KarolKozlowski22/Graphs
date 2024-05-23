use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::visit::IntoNodeReferences;
use rand::prelude::*;
use std::collections::HashMap;

pub fn page_rank_a(graph: &DiGraph<(), ()>, d: f64, iterations: usize, num_walks: usize) -> Vec<(String, f64)> {
    let mut rng = thread_rng();
    let mut visit_count = vec![0; graph.node_count()];
    let nodes: Vec<NodeIndex> = graph.node_indices().collect();
    let num_nodes = nodes.len();
    let mut node_labels = HashMap::new();

    for (i, node) in graph.node_references().enumerate() {
        node_labels.insert(node.0.index(), i.to_string());
    }

    for _ in 0..num_walks {
        let mut current_node = nodes[rng.gen_range(0..num_nodes)];
        for _ in 0..iterations {
            visit_count[current_node.index()] += 1;
            if rng.gen::<f64>() < d {
                // Teleportation step
                current_node = nodes[rng.gen_range(0..num_nodes)];
            } else {
                let neighbors: Vec<_> = graph.neighbors(current_node).collect();
                if neighbors.is_empty() {
                    // If no neighbors, teleport
                    current_node = nodes[rng.gen_range(0..num_nodes)];
                } else {
                    // Randomly walk to a neighbor
                    current_node = neighbors[rng.gen_range(0..neighbors.len())];
                }
            }
        }
    }

    // Normalize the visit counts to get the PageRank probabilities
    let total_visits: usize = visit_count.iter().sum();
    let mut ranks = HashMap::new();
    for (i, &count) in visit_count.iter().enumerate() {
        let label = node_labels.get(&i).unwrap().clone();
        ranks.insert(label.clone(), count as f64 / total_visits as f64);
    }

    // Sort ranks by values in descending order
    let mut sorted_ranks: Vec<_> = ranks.into_iter().collect();
    sorted_ranks.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    
    sorted_ranks
}
