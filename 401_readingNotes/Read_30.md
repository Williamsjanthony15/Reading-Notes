## Read 36 to spare confusion 


Whiteboard-style interviews are ubiquitous in the tech industry. For those who not had the pleasure, whiteboard interviewing is the practice of asking candidates to solve technical questions on a whiteboard, piece of paper, or computer during the interview. This kind of environment can feel like a pressure cooker and cause even the most competent engineer to fall apart.

In this article, I intend to pass along the best advice I ever received for going through a whiteboard interview. Note that I do not intend to address the fairness or efficacy of whiteboard interviews because, well, as interviewees we currently have to deal with them regardless.

## The Advice: Communicate!

The best piece of technical interview advice I have received and can impart upon you is to communicate, communicate, communicate! This may seem like an anti-climactic piece of advice, but I hope to be able to demonstrate to you that it’s actually the most important skill to prepare prior to an interview.

#### Note: as I discuss examples in the rest of this article, they will have a software engineering slant as it is the most familiar domain to me. Despite that slant, you can apply these skills to any whiteboard-style interview.

## What Do You Mean Communicate?
Let’s say you are in the interview and your interviewers throw you a whiteboard question. Do you step up to the whiteboard and feverishly start solving the problem?

No!

That tends to be everyone’s instinct, but it’s definitely not the right way to go. Even if you think you understand the problem, you should take some very important steps before moving forward.

### 1. First, Restate the Question

Do you understand what they’re asking you to do? Prove it. Restate the question for them and seek affirmation. You might actually be surprised to find you don’t fully understand what they’re asking for — perhaps the question is similar, but not the same, as a practice problem you have completed in the past. Using the tried-and-true fizz-buzz example, you could restate the problem as follows:

“So I’d like to restate the problem to you to make sure I understand what you’re looking for. The sole parameter for my function will be an integer. The sole output of my function will be an incrementing array, starting from the number 1 and ending at the input number.
If a number is a multiple of 3, the output will instead be `fizz`. If a number is a multiple of 5, the output will instead be `buzz`. However, if the output is a multiple of both 3 and 5, the output will instead be `fizzbuzz`. Is my understanding correct?”
The interview should give you affirmation or, perhaps, your understanding is incorrect and they will help you understand. There is no situation in which restating the problem will hurt you — it shows you can articulate a problem and gives you time to think it through a bit while you discuss. Furthermore, starting the discussion this way will help quell some nerves that might otherwise manifest while trying to solve the actual challenge.





### 2. Ask About Edge Cases

It’s still not time to dive right into coding the solution. Think for a bit about the inputs and expected output and think about potential edge cases to the problem. Ask about them. In many cases, the interviewer hasn’t even thought about edge cases and will make something up. That’s great — it shows you’re analytical and will work hard to try to prevent bugs (which often crop up due to edge cases).

Let’s use the fizz-buzz example. After successfully restating the problem, a valid way to ask about edge cases would be as follows:

“Now that I confirmed my understanding of the problem, I’d like to ask about some potential edge cases. Is it possible that the input would be a type other than a number? If so, what should the function do? Can the input be 0 or negative? Again, if so, what should the function do?”





### 3. Ask About Test Cases
This is free and you should take advantage of it. Simply ask if there are any test cases that the function should pass. Your interviewer might be expecting you to ask this question, so it might be necessary. But it’s also possible the interviewer was not expecting the question and will think “ah, this candidate knows about testing!”


### 4. Write Pseudocode and Ask If It Makes Sense
(Write Pseudocode and Check Your Logic)

Again, you don’t actually want to start writing code in an actual language. You’ll find yourself constrained by trying to remember the methods or other idiosyncrasies of the language rather than trying to come up with the correct logic. Instead, let your interviewer know you’re going to start by writing pseudocode and fill in the actual code later. (Coincidentally, this is a reasonable way to write actual code as well).


### ** Here’s the kicker: you can ask if your pseudocode makes sense to the interviewer. It’s possible they will be the type that doesn’t want to “give you hints,” but it’s also possible they’ll be more interested in how you think and want to discuss your pseudocode with you. When I interview candidates, I’m more interested in the latter — rarely do we ever actually develop software in a vacuum. **

In other words, in the worst case the interviewer will tell you to continue without actually offering feedback. In the best case, the interviewer might actually point out logical flaws in your pseudocode that will give you some serious benefit when transitioning to actual code.

Super bonus: If your pseudocode looks good but you end up having difficulty translating it to actual code, you have actually earned a lot of points by now! Sure, in some elite companies they won’t accept anything but functional code, but simply being able to reason through the pseudocode is sufficient for many great companies.

In keeping with our fizz-buzz example, let’s say we came up with the following pseudocode. We’ll ultimately be writing our code in javascript, but it hardly matters at this point.

*Example* 
function fizzBuzz(n) {
 // If n is not a number or not an integer greater 
 // than zero, return null
 
 // create empty array to store output
 
 // Loop through numbers from 1 to n
 
  // If number modulo 3 is zero, add ‘fizz’ 
  // to output array
  // Else If number modulo 5 is zero, 
  // add ‘buzz’ to output array
  // Else If number modulo 3 is zero and 
  // number modulo 5 is zero, add ‘fizzbuzz’ 
  // to array
  // Else add the number to the array
 
 // return output array
}

At this point, you might realize that you’d never get to the third `else-if` statement. Alternatively, when you confirm your pseudocode with interviewer, they might offer that up to you for free (seriously). In that case, you can rewrite your pseudocode to make sure you check the third condition first:

* EXAMPLE *
function fizzBuzz(n) {
 // If n is not a number or not an integer greater 
 // than zero, return null
 
 // create empty array to store output
 
 // Loop through numbers from 1 to n
  // If number modulo 3 is zero and 
  // number modulo 5 is zero, add ‘fizzbuzz’ 
  // to array
 
  // Else If number modulo 3 is zero, add ‘fizz’ 
  // to output array
  // Else If number modulo 5 is zero, 
  // add ‘buzz’ to output array
  // Else add the number to the array
 
 // return output array
}

### 5. Write the Actual Code and Ask if it Looks Good

(Finally Start Writing Code)

You should now convert your pseudocode into actual code. You don’t even need to remove the comments. At this point, you just need to plug the appropriate code for your language in. If you forget some syntax or a method name, you should be able to ask your interviewer for this information without too much grief. If they give you trouble, just say you’ll leave it as pseudocode for now.

*EXAMPLE*
function fizzBuzz(n) {
 if (isNaN(n) || !Number.isInteger(n) || n < 1) return null;
 let output = [];
 for (let i = 1; i <= n; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
   output.push(“fizzbuzz”);
  } else if (i % 3 === 0) {
   output.push(“fizz”);
  } else if (i % 5 === 0) {
   output.push(“buzz”);
  } else {
   output.push(i);
  }
 }
 
 return output;
}

At this point, don’t hesitate to ask if your solution looks good! If it doesn’t they might offer some tips to improve it. All of this communication scores points for you — you’ll seem articulate and easier to work with if you’re willing to objectively discuss ways to improve your work.



### 6. Stuck? Ask for Help!
(Ask for Help!)

If you’re having trouble along the way, it’s not illegal to ask for some help. Just phrase it conversationally. For example:

“I’m a bit stuck here, do you have any tips to nudge me in the right direction?”
The answer might be “no, I’d like to see if you can solve it from here on your own,” but it also very well might be a “yes” with a useful tip!

Bonus: Communicating Prior to the Interview
You should have a human resources or interview point of contact prior to the interview. Are you curious whether there will be a coding portion of the interview? Ask them! Furthermore, you can ask if there is anything in particular you should prepare. They very well might give you hints like specifying the language in which they’ll ask questions, the number of questions, the style of question (e.g., develop an algorithm vs. find the bug). They might tell you whether you’ll be sitting at a computer or standing at a whiteboard — very useful information you might be able to use to practice or, at the very least, mentally prepare.


# We’re All Human
Above all, remember that we’re all human. Your interviewer has been in your position and understands the stress of a technical interview. Your interviewer has probably seen quite a few candidates sweating it out, but possibly very few open who openly discuss problems in a conversational manner. If you can achieve this, you’ll be in great shape.


What Has Your Experience Been?
Have you been in a technical interview where communication saved you? Have you had the opposite experience? Let me know in the comments! I’d love to hear about your experiences.

#### Some / all of these notes have been taken directly from https://hackernoon.com/the-best-whiteboard-interview-advice-i-ever-received-3ebbfa72e4a
