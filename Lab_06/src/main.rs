mod draw_graph;
mod page_rank_a;
mod page_rank_b;
mod read_graph_from_file;

pub use crate::draw_graph::draw_graph;
pub use crate::page_rank_a::page_rank_a;
pub use crate::page_rank_b::page_rank_b;
pub use crate::read_graph_from_file::read_graph_from_file;

use std::iter::zip;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let filename = "src/data/example_graph_2.dat";
    let graph = read_graph_from_file(filename).expect("Failed to read graph from file");

    let d = 0.15;
    let iterations = 1000;
    let num_walks = 1000000;
    let tolerance = 1e-6;
    
    let ranks_a = page_rank_a(&graph, d, iterations, num_walks);
    let (ranks_b, iters) = page_rank_b(&graph, d, iterations, tolerance);

    println!("PageRank A (Random Walks)\t\tPageRank B (Matrix Multiplication) after {} iterations", iters);
    for ((node_a, rank_a), (node_b, rank_b)) in zip(ranks_a.iter(), ranks_b.iter()) {
        print!("Wierzchołek {} ==> PageRank = {:.6}\t", node_a, rank_a);
        println!("Wierzchołek {} ==> PageRank = {:.6}", node_b, rank_b);
    }

    draw_graph(&graph, "graph.png")?;

    Ok(())
}