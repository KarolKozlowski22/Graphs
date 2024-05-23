use petgraph::graph::DiGraph;
use std::fs::File;
use std::io::Write;
use std::path::Path;
use petgraph::dot::{Dot, Config};

pub fn draw_graph(graph: &DiGraph<(), ()>, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
    let dot_graph = Dot::with_config(
        graph, 
        &[Config::EdgeNoLabel, Config::NodeIndexLabel]
    );

    let dot_file_path = Path::new("graph.dot");
    let mut file = File::create(&dot_file_path)?;
    write!(file, "{:?}", dot_graph)?;

    // std::process::Command::new("sed")
    //     .args(&["-i", "s/\\[ \\]//g", dot_file_path.to_str().unwrap()])
    //     .output()?;

    std::process::Command::new("dot")
        .args(&["-Tpng", dot_file_path.to_str().unwrap(), "-o", filename])
        .output()?;

    Ok(())
}
