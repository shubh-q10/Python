def markdown_to_html_image(markdown_image: str) -> str:
    alt_start = markdown_image.find('[') + 1
    alt_end = markdown_image.find(']')
    url_start = markdown_image.find('(') + 1
    url_end = markdown_image.find(')')
    
    alt_text = markdown_image[alt_start:alt_end]
    image_url = markdown_image[url_start:url_end]
    

    
    return (f'<img src="{image_url}" alt="{alt_text}">')

print(markdown_to_html_image("![awesome dog](dog.jpg)"))
