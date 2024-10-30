---
title: Advanced Robotics (2023 Spring)
date: 2022-10-10
type: landing

sections:
  - block: markdown
    content:
      title: Advanced Robotics (2022 Fall)
      subtitle: Robotics Course for undergrad and grad students
      text: | 
        
        ## General Description

        This course is structured into three segments: A) Robot Mechanics, B) Dynamics & Control C) Planning & Perception. First, learners will be familiarized with the fundamentals relevant to the course, namely, homogeneous transformations, forward and inverse kinematics, velocity kinematics and eventually acquainted to the essentials including robot dynamics and controls. Finally, applied topics related to robot planning and perception covering path and motion planning, image formation, processing and analysis, vision-based control and image-guided robotics will be introduced to learners relating the fundamentals and essentials acquired in the earlier part of the course

        ## Course Objective
        The goal of this course is to introduce students to the basic concepts in robotics that 
        * provide prerequisite knowledge for follow-on courses, 
        * (b) provide essential knowledge of the field that would be required by a practicing engineer who must deal with automation, and 
        * (c) provides professional development by introducing best practices and ethical considerations for engineering design. 
        
        This course also includes a significant laboratory component.

        ## Lecture Information
        ### Instructors
        Katie Driggs-Campbell, {{% mention "liangjingyang" %}}(liangjingyang@intl.zju.edu.cn)
        ### Lead TA
        Lead TA：{{% mention "songjiexiao" %}}
        ### Lectures
        Mon and Wed, 8-920 am (West Hall C105/111) 
        ### Lab
        See lab grouping, E205
        ### Consultation Hour
        - Tues 1830-2000 (Even Wk)
        - Thurs 1530-1700 (Odd Wk); 
        - @E205 Instructional Control Lab (Welcome also to arrange a time with us) 
        ### Prerequisite
        One of MATH 225, MATH 286, MATH 415, MATH 418
        ###  Reference Textbook
        - John J. Craig, Introduction to Robotics: Mechanics and Control (4th Edition), Pearson, 2018. ISBN-10: 0133489795 
        - Lynch & Park, Modern Robotics: Mechanics, Planning and Control (1st Edition), Cambridge University Press, 2017. ISBN-10: 1107156300 
        - Peter Corke, Robotics, vision and control: fundamental algorithms in MATLAB® (2nd Edition), Springer, 2017. ISBN-10: 3319544128
        ### Assesment
        - Homework: 20%
        - Labs/Projects: 20%
        - Midterm: 20%
        - Final: 40%
        ## Overview of Course Schedule
        ```mermaid
        gantt
          dateFormat  YYYY-MM-DD
          section Lecture
          Robot Mechanics           :a1, 2023-02-15, 28d
          Dynamics and Control      :a2, after a1 , 28d
          Rvision and Midterm       :a3, after a2 , 7d
          Planning and Perception   :a4, after a3, 28d
          Revision Overall              :a5, after a4, 7d
          Reading/Exam              :a6, after a5, 7d
          Exam                      :a7, after a6, 7d
          section Lab
          Lab on Robot Mechanics          :l1, 2023-02-22  , 21d
          Lab on Dynamics and Control     :l2, after l1 , 21d
          Lab on Planning and Perception  :l3, after a3, 14d 
        ```
        <div align=center> <!-- To put the figures below cetered. -->
        {{< figure src="ece470_2022_spring_schedule.png" caption=" A Detailed Schedule for ECE470 2023 Spring" numbered="true" >}}

        {{% callout note %}}
        You can find more resources of this course [here](https://learn.intl.zju.edu.cn/webapps/blackboard/content/listContent.jsp?course_id=_2349_1&content_id=_80072_1&mode=reset)
        {{% /callout %}}


    design:
      # See Page Builder docs for all section customization options.
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
---