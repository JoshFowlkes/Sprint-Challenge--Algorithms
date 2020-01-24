#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) While 'a' is less than 'n^3',  'a' will increment by 'n^2'. SO using an example of 'n=3', while 'a' is less than 27, this loop will increment from 0, 9, 18, 27, and thus the loop runs 3 times. So the loop will run 'n' number of times. Fairly linear, so this would be a case of 'O(n)'.


b) This one contains two loops. The for loop will run for i in range(n) and continue to increment by 1. Whereas the inner while loop will run within the for loop while j is less than n and double every time. Then will circle back to the for loop and repeat until the for loop has reached range(n). So the outer for loop is growing at a linear rate as it increments by 1. The inner while loop is doubling everytime. Since it is doubling everytime itll grow rapidly overtime, not as rapidly as it would if it was being squared(O(n^2)), and its faster than the linear O(n), so since it lies in between those two, it should be growing at O(nlog(n)).


c) So this one, looking at the return statement it has a recursive loop. The only condition before it is to return 0 if the parameter passed is so. So this is returning essentially 2 + (2 + bunnies - 1). So there are only additions and subtractions going on, and it's only going to run for n number of times(or bunnies in this case lol). So this is fairly linear in time complexity, so O(n).

## Exercise II
So since we're trying to determine if an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f, given that we're searching for a range, I would assume that a binary search would be the ideal approach here. 

So if the parameter you're passing is n(for number of floors), start with  n // 2(since we're going by floors they have to be whole numbers so using integer division instead of floating), and hypotehtically drop it from half way down the building(n // 2). If it breaks then you know the max height is less than n // 2, if it does not break then you know the max height is above n // 2. and depending on which one contains the breaking point, you'd then divide that half // 2 and repeat the process until reaching the integer indicative of the floor number. Or if this was going by number of feet, then could use floating division for very high accuracy. Either way, this would be a fairly linear process of just iterating through these binary searches, so the time complexity would be O(n). 

