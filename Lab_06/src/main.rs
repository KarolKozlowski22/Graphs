mod draw_graph;
mod page_rank;
mod read_graph_from_file;

pub use crate::draw_graph::draw_graph;
pub use crate::page_rank::page_rank;
pub use crate::read_graph_from_file::read_graph_from_file;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let filename = "src/data/example_graph.dat";
    let graph = read_graph_from_file(filename).expect("Failed to read graph from file");

    let d = 0.15;
    let iterations = 1000;
    let num_walks = 1000;
    
    let ranks = page_rank(&graph, d, iterations, num_walks);

    for (node, rank) in ranks.iter() {
        println!("Wierzchołek {} ==> PageRank = {:.6}", node, rank);
    }

    draw_graph(&graph, "graph.png")?;

    Ok(())
}