Steps to run and description about the program.....

There is a python notebook named Wiz_Mantra, which needs to be opened in python for running the program, all the files and dependenices are in the folder itself.

Now it imports an image 'rss.jpg' for main answer sheet and one template image named as 'Tick.jpg', these can be changed accordingly, to get the different output. Main idea used is template matching function of opencv so the template image is run over the main image and if match according to a adjustable threshold, we store the coordinates of the images' upper left coordinate. Now we iterate these points and check in which one fourth part it exists.so, for each corresponding postion a error array(Error) element will be accessed. and so the corresponding error will be stored in an array (d) representing errors of the user. Then at last we iterate the array and count the respective errors and print them on the console.

.
.
.
.
.
.
.

For the Second part some approaches with bayesian networks

Downloading bayespy library for constructing a bayesian network of 
the given data generated in part 1
Then implementing some D-SEPARATION algo on this bayesian network to find the largest subset which are all independent from most of the other elements as they will be the elements at the top of the concept tree formed and correcting these error codes will help in rectifying all the other errors(95%).

Other approaches to this problem can be using multinomial bayes algorithm  in  which for each training set we get real time probability of all error codes and corresponding to this the error code with maximum probability will gives us the required answer.

