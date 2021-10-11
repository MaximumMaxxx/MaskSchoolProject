<h1>Max's Mask Code</h1>

Repl: If you want to run it in your browser: https://replit.com/@MaxwellWindland/Max-s-Magnificent-Mask-Caclculating-Code-#README.md


This is a series of programs made my Max for a math project on optomization. The goal was that students would
Come up with their own creative solutions to the same problem. You also had to prove that you had the best solution in a way to convince your classmates.
Some approaches included google sheets, desmos, and trial and error.
For this I only planned to write one program: Ratio Check. However I was at a horse show for the weekend with nothing to do so I came up with 2 more ways
to solve it. This folder is now what that is. All files run indepenantly of any libraries only requiring python. They do have some nice formatting code at the
bottom which is the same and uses the built in math library but that's about it.

How we got here: Initially I attempted to do this project in desmos however my lack of knowledge on how to use desmos I failed.
The one key thing I got from that was the idea of expressing the number of masks and clips as simply a ratio between the two numbers.
In desmos this ratio was used for graphing however in the final solution it's used instead to feed into a function which does a bunch of calulations to find the maximum that that ratio can produce while staying in the limits.

My First Crack at this problem (Ratio Check) produced the aforementioned function. In it I loop through every different ratio between all clips and no clips. 
For some reason it runs faster than a similar but different implementation and I'm not sure why. 

My Second Attempt produced mega brute the easiest to understand but the least interesting and slowest of all the implementations. It bassicaly just checks 33 million combos to see if they work. It's bad and dumb and slow and for that reason I dislike it. The code is easy to understand though so I guess that's a plus.

After my disapointment at my second solution I came up with search algo. Now the previous apporaches took a few minutes to work but seach algo is built different. 
It runs in .5 - 5 seconds depending on which computer I use. 
Search algo takes the same main function from Ratio Check but instead of checking every ratio it checks like 15 strategic ones and finds the right answer quickly. 
If you know what binary search is its similar. More specific details are in the code comments (The big lines of english that start with #) however this bassically eliminates 50% of the possible numbers a few times until it very quickly finds the best answer.

IF YOU WANT MORE DETAILS OR JUST WANT TO LOOK AT THE CODE ALL THE SOURCE CODE FILES ARE ALSO HERE
