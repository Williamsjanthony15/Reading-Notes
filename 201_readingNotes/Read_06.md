# Reading Notes for Day 6.

<ul>
  <li>HTML links</li>
      <li>Chapter 4 Links</li>
        <li>Links are the defining feature of the web. They allow you to move from one web page to another - enabling the very idea of browsing or Surfing.</li>
        <li>Links can be:
          <li>One website to another.</li>
          <li>links from one page to another on the SAME website.</li>
          <li>links from one part of a web page to another part of the same website.</li>
          <li>links that open new browser windows.</li>
          <li>links that start up your email program and address a new email to someone... The potential is endless.</li>
<li> writing links - Writing links are created by using the <a> element. Users can click on anything between the opening <a> tag and the closing </a> tag. you specifiy which page you want to link to using the HREF attribute.</li>
<li> EXAMPLE :: <a href = "https://www.google.com/?client=safari">Google</a></li>

<ul>
  <li> Ways to utilize links </li>
    <li> using the "a" element using the HREF attribute. Users can click on anything that appears between the opening "a" tag and the closing "a" tag. When you link to a different website, the value of the href attribute will be the full web address for the site, which is known as an absolute URL.</li>
    <li> Linking to other pages on the same site is also done with the "a" element, but rather than specifying the domain name in the url you can use a shorthand known as a "relative" url. If all of your pages are in the same folder, your HREF just has to be the name of the file. You can also do it from other folders but the syntax would be different.</li>
  <li> Directory Structure</li>
    <li> Structure </li>
      The top level folder is know as the root folder. The Root folder contains all of the other files and folders for a website. Each section of the site is placed in a seperate folder, this helps organize the files.
    <li> Relationships </li>
      The relationship between files and folders on a website is described using the same terminology as a family tree. There are parent and children folders. 
    <li> HomePages </li>
      The main homepage of a site written in HTML is called "index.html". Web servers are usually set up to return the index.html file if no file name is specified. Therefore if you enter examplearts.com it will return examplearts.com/index.html. 
</ul>

  <li>CSS Layouts</li>

  <ol>
  <li> Block level elements </li>
    <li> H1, p, ul , li </li>
  <li>inline elements</li>
    <li> img, b, i </li>
  <li> Controlling the position of elements</li>
  <ul>
    <li>Normal flow </li>
    <li>Relative Positioning </li>
    <li>Absolute Positioning </li>
    <li>Fixed Positioning </li>
    <li>Floating Elements</li>
  </ul>
  <p>
  Keep in mind, Screen sizes, screen resolution, Page sizes, Fixed Width Layouts, and Liquid Layouts.
  </p>

Chapter 15 Layouts

  <li>JS Functions</li>

Chapter 3 Functions, Methods, and Objects
  <ul>
    <li>Functions & Methods</li>
      Functions let you group a series of statments together to perform a specific task. If different parts of a script repeat the same taks, you can reuse the function(rather than repeating the same set of statment(s)).
      <li> Declaring a function</li>
      To create a function you give it a name and than write the statements needed to archeive its task inside the curly braces. This is known as a Function declorations.
      IE: function sayHello() {
        document.write('hello!');
      }
      <li>Calling a function</li>
        Having declared the function you can then execute all of the statments between its curly braces with just one line of code. This is known as "calling the function."
        IE: sayHello();
    <li>Objects</li>

Article "6 reasons for pair programming"

<li>How does pair programming work?</li>
  pair programming commonly involves two roles: the Driver and the Navigator. Driver is the programmer who is typing and the only one whose hands are on the keyboard. Handling the “mechanics” of coding, the Driver manages the text editor, switching files, version control, and—of course writing—code. The Navigator uses their words to guide the Driver but does not provide any direct input to the computer. The Navigator thinks about the big picture, what comes next, how an algorithm might be converted in to code, while scanning for typos or bugs. The Navigator might also utilize their computer as a second screen to look up solutions and documentation, but should not be writing any code.
</li>
<li>
Why pair program?

While learning to code, developers likely study several programming languages. Similar to a foreign language class, there are four fundamental skills that help anyone learn a new language: Listening: hearing and interpreting the vocabulary Speaking: using the correct words to communicate an idea Reading: understanding what written language intends to convey Writing: producing from scratch a meaningful

Pair programming touches on all four skills: developers explain out loud what the code should do, listen to others’ guidance, read code that others have written, and write code themselves.

During a five-hour paired lab session, Code Fellows students work on all four of these language-specific skills. The abilities they foster will serve them well in completing assignments, in their own communication and learning, in interviews, and in readiness for a job at a company that utilizes this agile practice.

Wow, all that? Let’s take a look!

1. Greater efficiency

It is a common misconception that pair programming takes a lot longer and is less efficient. In reality, when two people focus on the same code base, it is easier to catch mistakes in the making. Research indicates that pair programing takes slightly longer, but produces higher-quality code that doesn’t require later effort in troubleshooting and debugging (let alone exposing users to a broken product). So, in the long-run, it’s often actually more efficient than two people working on separate features. When coming up with ideas and discussing solutions out loud, two programmers may come to a solution faster than one programmer on their own. Also, when the pair is stuck, both programmers can research the problem and reach a solution faster. Researches also identified pairing enhances technical skills, team communication, and even enjoyability of coding in the workplace.

2. Engaged collaboration

When two programmers focus on the same code, the experience is more engaging and both programmers are more focused than if they were working alone. It is harder to procrastinate or get off track when someone else is relying on you to complete the work. Popping open your Facebook timeline is just that less enticing when someone else is looking at your screen.

Another important aspect of learning to program is knowing when to ask for help. We advise our students to spend no more than fifteen minutes stuck on a problem before asking a teaching assistant or instructor for help. When developers pair program, they rely more on each other and can often find a solution together without needing to ask for additional help. Ultimately, this boosts overall confidence.

3. Learning from fellow students

Everyone has a different approach to problem solving; working with a teammate can expose developers to techniques they otherwise would not have thought of. If one developer has a unique approach to a specific problem, pair programming exposes the other developer to a new solution.

Often times, the developers in a pairing have different skill sets. If one programmer is more experienced in a certain skill, they can teach a student who is less familiar with that area. The less experienced developer benefits from the experienced developer’s knowledge and guidance, and the latter benefits from explaining the topic in their own words, further solidifying their own understanding.

4. Social skills

Pair programming is great for improving social skills. When working with someone who has a different coding style, communication is key. This can become more difficult when two programmers have different personalities. Pair programming not only improves programming skills, but can also help programmers develop their interpersonal skills. When just grabbing the keyboard and taking over isn’t an option, getting good at finding the right words is a skill unto itself.

This has long-term career impacts. As much as employers want strong programmers, they know it’s essential to hire people who can work well with others.

5. Job interview readiness

A common step in many interview processes involves pair programming between a current employee and an applicant, either in person or through a shared screen. They will carry out exercises together, such as code challenges, building a project or feature, or debugging an existing code base. By doing so, companies can get a better feel for how an applicant will fit into the team and their collaboration style.

For most roles, the ability to work with and learn from others and stellar communication skills are as (or more!) important to a company than specific technical skills. Pair programming strengthens all of those skills.

6. Work environment readiness

Many companies that utilize pair programing expect to train fresh hires from CS-degree programs on how they operate to actually deliver a product. Code Fellows graduates who are already familiar with how pairing works can hit the ground running at a new job, with one less hurdle to overcome.

</li>

Giving credit to 

https://www.codefellows.org/blog/6-reasons-for-pair-programming/ 

Written by Allie Grampa, august 24 2018. 