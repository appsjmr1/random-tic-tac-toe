# Random Tic Tac Toe


<p align="left"><img src="Gears.png" alt="drawing" width="140"/>In The American Mathematical Monthly Vol. 66, No. 2 (Feb., 1959), pp. 144-145, T.M. Little provided an answer to a question that had been posed in the same journal in 1958 by F.E. Clark. The question (written much more elegantly than this by Clark) was, what percent of the time would each possible tic tac toe outcome occur given random play? It was assumed X moves first. The exact outcome proportions, up to three figures, were <img src="/tex/421e6a4f856529e0e813eaba9c05d8cd.svg?invert_in_darkmode&sanitize=true" align=middle width=74.19175169999998pt height=22.465723500000017pt/>, <img src="/tex/9bbf9cf23d242f1eaa90b3155fad61c4.svg?invert_in_darkmode&sanitize=true" align=middle width=72.86953079999999pt height=22.465723500000017pt/>, and <img src="/tex/65d5c7635122853a118282ef4c8ef96a.svg?invert_in_darkmode&sanitize=true" align=middle width=72.05072324999999pt height=22.465723500000017pt/>. Parenthetically, if you noticed the LaTeX font and are wondering how to get it on a GitHub README file, you can use a handy tool called <a href="https://github.com/apps/texify">TeXify</a>. Back to the main story: the code in this repository will run one million games with random moves, X always playing first. You can clone the repository and test it yourself by executing </p>
<div>
 
```python main.py```
 
 </div>


<p>
from the command prompt: When you execute the above commend, just make sure you are in the random_tic_tac_toe directory you will have after running the below git clone call. In case you are just getting started, you will want to first see the prerequisites section, also below. The outcome proportions for a run of main.py, rounded to three figures, were <img src="/tex/421e6a4f856529e0e813eaba9c05d8cd.svg?invert_in_darkmode&sanitize=true" align=middle width=74.19175169999998pt height=22.465723500000017pt/>, <img src="/tex/9bbf9cf23d242f1eaa90b3155fad61c4.svg?invert_in_darkmode&sanitize=true" align=middle width=72.86953079999999pt height=22.465723500000017pt/>, and <img src="/tex/65d5c7635122853a118282ef4c8ef96a.svg?invert_in_darkmode&sanitize=true" align=middle width=72.05072324999999pt height=22.465723500000017pt/>. Consistent with Little's solution.</p>

<P>Shortly I will post an add-on which allows the program to learn from its mistakes so that X never looses.</P>


## Installing

### Prerequisites
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org)

### Download repository

<p> To download the repository, type the following from the command line of your operating system:</p>
<div>
 
```git clone https://github.com/appsjmr1/random_tic_tac_toe.git```
 
 </div>
