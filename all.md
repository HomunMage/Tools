---
layout: base
---

# all notes


<ul>
    {% assign filtered_pages = site.pages %}
    {% for page in filtered_pages %}
        {% if page.title %}
            <li><a href="{{ page.url | prepend: site.baseurl }}">{{ page.title }}</a></li>
        {% endif %}
    {% endfor %}
</ul>
