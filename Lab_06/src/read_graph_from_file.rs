use std::fs::File;
use std::io::{self, BufRead};
use petgraph::graph::DiGraph;
use std::collections::HashMap;

pub fn read_graph_from_file(filename: &str) -> io::Result<DiGraph<(), ()>> {
    let mut graph = DiGraph::new();
    let mut node_map = HashMap::new();
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<String> = line.split(':').map(|s| s.trim().to_string()).collect();
        if parts.len() != 2 {
            continue;
        }
        node_map.insert(graph.add_node(()), parts[0].clone());
    }

    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split(':').collect();
        if parts.len() != 2 {
            continue;
        }
        let src_label = parts[0].trim();
        let dest_labels: Vec<&str> = parts[1].split(',').map(|s| s.trim()).collect();
        
        let src_node = *node_map.iter().find(|(_, &ref v)| v == src_label).unwrap().0;

        for dest_label in dest_labels {
            let dest_node = *node_map.iter().find(|(_, &ref v)| v == dest_label).unwrap().0;
            graph.add_edge(dest_node, src_node, ());
        }
    }

    Ok(graph)
}