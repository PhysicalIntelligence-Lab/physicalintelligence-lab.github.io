---
# Leave the homepage title empty to use the site title
title:
date: 2024-09-01
type: landing

sections:
  - block: slider
    content:
      slides:
      - title:  Welcome to the Hua Chen Research Group
        content: 这里的照片感觉可以放合影，以后有视频也可以放视频
        align: center
        background:
          image:
            filename: zjui_scene.jpg
            filters:
              brightness: 0.7
          position: right
          color: '#666'
      - title: Lunch & Learn ☕️
        content: 'Share your knowledge with the group and explore exciting new topics together!'
        align: left
        background:
          image:
            filename: zjui_scene.jpg
            filters:
              brightness: 0.7
          position: center
          color: '#555'
      - title: World-Class Semiconductor Lab
        content: 'Just opened last month!'
        align: right
        background:
          image:
            filename: zjui_scene.jpg
            filters:
              brightness: 0.5
          position: center
          color: '#333'
        link:
          icon: graduation-cap
          icon_pack: fas
          text: Join Us
          url: ../contact/
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
      title: | 
        
      image:
        filename: logo.png
        position: center
      text: |
        <br>
        
        Group Introduction 
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit,
        vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida
        mauris. Nam arcu libero, nonummy eget, consectetuer id, vulputate a, magna.
        Donec vehicula augue eu neque. Pellentesque habitant morbi tristique senectus
        et netus et malesuada fames ac turpis egestas. Mauris ut leo. 

    design:
      background:
      # Choose colors such as from https://html-color-codes.info
          gradient_start: '#013ADF'
          gradient_end: '#58FAF4'
          gradient_angle: 90
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
      view: compact
      columns: '2'

  - block: collection
    content:
      title: Latest Events
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
      page_type: event
      text:  
    design:
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
      view: citation
      columns: '2'


  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team" %}}
    design:
      columns: '1'

---
