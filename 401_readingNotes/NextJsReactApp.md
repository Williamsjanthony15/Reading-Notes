Read 36 to spare confusion

# Create Next.js react app

## Setup
First, let’s make sure that your development environment is ready.

If you don’t have Node.js installed, install it from here. You’ll need Node.js version 10.13 or later.
You’ll be using your own text editor and terminal app for this tutorial.
If you are on Windows, we recommend downloading Git for Windows and use Git Bash that comes with it, which supports the UNIX-specific commands in this tutorial. Windows Subsystem for Linux (WSL) is another option.

Create a Next.js app
To create a Next.js app, open your terminal, cd into the directory you’d like to create the app in, and run the following command:

npx create-next-app nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/master/basics/learn-starter"
Under the hood, this uses the tool called create-next-app, which bootstraps a Next.js app for you. It uses this template through the --example flag.

If it doesn’t work, please take a look at this page.

Run the development server
You now have a new directory called nextjs-blog. Let’s cd into it:

cd nextjs-blog
Then, run the following command:

npm run dev
This starts your Next.js app’s "development server" (more on this later) on port 3000.

Let’s check to see if it’s working. Open http://localhost:3000 from your browser.

Editing the Page
Let’s try editing the starter page.

Make sure the Next.js development server is still running.
Open pages/index.js with your text editor.
Find the text that says “Welcome to” under the <h1> tag and change it to “Learn”.
Save the file.
As soon as you save the file, the browser automatically updates the page with the new text:

# Tailwind CSS

## Example Code 

<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <h4 class="chat-notification-title">ChitChat</h4>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification {
    display: flex;
    max-width: 24rem;
    margin: 0 auto;
    padding: 1.5rem;
    border-radius: 0.5rem;
    background-color: #fff;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
  .chat-notification-logo-wrapper {
    flex-shrink: 0;
  }
  .chat-notification-logo {
    height: 3rem;
    width: 3rem;
  }
  .chat-notification-content {
    margin-left: 1.5rem;
    padding-top: 0.25rem;
  }
  .chat-notification-title {
    color: #1a202c;
    font-size: 1.25rem;
    line-height: 1.25;
  }
  .chat-notification-message {
    color: #718096;
    font-size: 1rem;
    line-height: 1.5;
  }
</style>


## Exmaple Code

Some / all of these notes may have been taken from https://nextjs.org/learn/basics/create-nextjs-app
