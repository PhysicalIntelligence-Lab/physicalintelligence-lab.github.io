---
# Leave the homepage title empty to use the site title
title:
date: 2024-09-01
type: landing

sections:
  - block: slider
    content:
      slides:
      - title:  Welcome to the Physical Intelligence Lab
        content: 
        align: center
        background:
          image:
            filename: zjui_scene.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      # - title: Lunch & Learn ☕️
      #   content: 'Share your knowledge with the group and explore exciting new topics together!'
      #   align: left
      #   background:
      #     image:
      #       filename: zjui_scene.jpg
      #       filters:
      #         brightness: 0.7
      #     position: center
      #     color: '#555'
      # - title: World-Class Semiconductor Lab
      #   content: 'Just opened last month!'
      #   align: right
      #   background:
      #     image:
      #       filename: zjui_scene.jpg
      #       filters:
      #         brightness: 0.5
      #     position: center
      #     color: '#333'
      #   link:
      #     icon: graduation-cap
      #     icon_pack: fas
      #     text: Join Us
      #     url: ../contact/
    design:
      # Slide height is automatic unless you force a specific height (e.g. '400px')
      slide_height: ''
      is_fullscreen: true
      # Automatically transition through slides?
      loop: false
      # Duration of transition between slides (in ms)
      interval: 2000

# sections:
#   - block: markdown
#     content:
#       title: <font color=white> <br><br><br><br><br>**Hua Chen Research Group** </font>
#       subtitle: ''
#       text:  <font color=blue> 这个图片感觉可以放合影 </font>
#       position: left
#     design:
#       columns: '1'
#       background:
#         image: 
#           filename: zjui_scene.jpg
#           filters:
#             brightness: 1
#           parallax: true # make the section hidden by scrolling the wheel
#           position: center
#           size: cover
#           text_color_light: True
#       spacing:
#         padding: ['20px', '0', '20px', '0']
#       css_class: fullscreen

  - block: hero
    content:
      title: Introduction 
      text: |
        <br>
        Welcome to the Physical Intelligence Lab! Here, we merge the realms of robotics and machine learning to explore innovative solutions that enhance physical interaction with the world. Our research delves into intelligent systems that not only perform tasks but also learn and adapt in real-time, paving the way for advancements in automation, smart environments, and beyond.

    design:
      background:
      # Choose colors such as from https://html-color-codes.info
          gradient_start: '#003f88'
          gradient_end: '#eeeeee'
          gradient_angle: 45
          # Text color (true=light, false=dark, or remove for the dynamic theme color).
          text_color_light: true
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
      text:  
    design:
      # view: showcase 
      view: compact
      columns: '2'

  - block: collection
    content:
      text: ""
      title: Featured Publications
      count: 5
      filters:
        folders:
          - publication
        publication_type: ''
    design:
      view: compact
      columns: '2'

---
