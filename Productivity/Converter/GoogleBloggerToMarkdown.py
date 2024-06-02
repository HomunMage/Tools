import os
import re
import html2text

def read_xml_file(xml_file_path):
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_titles_and_contents(xml_content):
    xml_content = xml_content.replace('&lt;', '<').replace('&gt;', '>')
    titles = re.findall(r"<title type='text'>(.*?)</title>", xml_content)
    contents = re.split(r"<title type='text'>.*?</title>", xml_content)[1:]
    return zip(titles, contents)

def save_to_tmp_files(titles_and_contents, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for title, content in titles_and_contents:
        filename = f"{title}.md".replace(" ", "_").replace("/", "-")
        filepath = os.path.join(output_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Successfully saved content: {filepath}")
        except Exception as e:
            print(f"Failed to save content: {filepath}")
            print(e)

def convert_html_to_markdown(html_content):
    md_converter = html2text.HTML2Text()
    md_converter.ignore_links = False
    md_content = md_converter.handle(html_content)
    return md_content

def convert_tmp_files_to_md(output_dir):
    tmp_files = [f for f in os.listdir(output_dir) if f.endswith('.md')]

    for tmp_file in tmp_files:
        tmp_file_path = os.path.join(output_dir, tmp_file)
        md_file_path = os.path.join(output_dir, tmp_file.replace('.md', '.md'))

        with open(tmp_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        md_content = convert_html_to_markdown(html_content)

        try:
            with open(md_file_path, "w", encoding="utf-8") as file:
                file.write(md_content)
            print(f"Successfully saved content: {md_file_path}")
        except Exception as e:
            print(f"Failed to save content: {md_file_path}")
            print(e)


def make_md_files_clean(output_folder):
    md_files = [f for f in os.listdir(output_folder) if f.endswith('.md')]

    for md_file in md_files:
        md_file_path = os.path.join(output_folder, md_file)

        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove &nbsp; from the content
        content = content.replace('&nbsp;', '')

        content = content.replace('=&gt;', '')
        

        with open(md_file_path, 'w', encoding='utf-8') as file:
            file.write(content)


def main():
    xml_file_path = "./blog.xml"
    output_dir = "outputs"

    xml_content = read_xml_file(xml_file_path)
    titles_and_contents = extract_titles_and_contents(xml_content)
    save_to_tmp_files(titles_and_contents, output_dir)

        
    # Convert .tmp files to .md files
    convert_tmp_files_to_md(output_dir)


    make_md_files_clean(output_dir)

if __name__ == "__main__":
    main()