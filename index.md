---
layout: home
---
<div class="container">
  <h1>Posts</h1>
  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        {% assign date_format = "%Y-%m-%d" %}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h2>
          <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>
</div>
