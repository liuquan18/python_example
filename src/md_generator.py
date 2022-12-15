from mdutils.mdutils import MdUtils

#%%
def doc_quick_plots(file_name, title, plot_dir,):
    """
    function to generate the markdown file
    **Parameter**
        *file_name* the name of the markdown file you are gonna make.
        *title* the title in the markdown file.
        *plot_dir* the directory for the images that gonna include in the note.
    """
    md_file = MdUtils(file_name, title=title)  # qick plots

    # overview
    md_file.new_header(level=1, title="statistical overview")
    md_file.new_paragraph("Here is a simple example show how to"
                     "generator a markdown file with python scripts"
    )

    md_file.new_header(level = 1, title = 'Red Line plot')
    md_file.new_line(
        md_file.new_inline_image(
            text="red",
            path=plot_dir + "red_line.png",
        )
    )

    md_file.new_header(level = 1, title = 'Green line plot')
    md_file.new_line(
        md_file.new_inline_image(
            text="green",
            path=plot_dir + "green_line.png",
        )
    )

    # Create a table of contents
    md_file.new_table_of_contents(table_title='Contents', depth=2)
    md_file.create_md_file()