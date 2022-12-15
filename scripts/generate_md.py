import src.data_generator as data_generator
import src.md_generator as md_generator

file_name = "../docs/source/note_example.md"  # change here if the path not right
plot_dir = "./plots/"             # change the dir if the path not right

try:
    md_file = md_generator.doc_quick_plots(file_name,title = "example note", plot_dir = plot_dir)

except FileNotFoundError:
    "plots not found, run `make_plot` first"