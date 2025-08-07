
import markdown
import os

def convert_md_to_html(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            input_filepath = os.path.join(input_dir, filename)
            output_filename = filename.replace(".md", ".html")
            output_filepath = os.path.join(output_dir, output_filename)

            with open(input_filepath, "r", encoding="utf-8") as f:
                md_content = f.read()
            
            html_content = markdown.markdown(md_content)

            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Converted {filename} to {output_filename}")

if __name__ == "__main__":
    input_directory = "ielts_study_plan_website"
    output_directory = "ielts_study_plan_website"
    convert_md_to_html(input_directory, output_directory)


