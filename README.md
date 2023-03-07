<h1 align="center"><b>COMPMT: All-in-one MT Evaluation System</b></h1>
<h2>Section 01: Automatic Evaluation Webapp</h2>
For Automatic(BLEU, TER, METEOR) evaluation, COMPMT has a webapp based on streamlit. <br><br>
Were you just need to: <br>
[1] Enter you scholar id; <br>
[2] Insert the `gold.txt` &amp; `pred.txt` files; <br>
[3] Click on submit. <br>

it will show score for all 3 method. <br>

### Inputs
![alt text](https://raw.githubusercontent.com/human71/comp-mt/main/Inputs.png)

### Results
![alt text](https://raw.githubusercontent.com/human71/comp-mt/main/Result.png)


<h2>Section 02: Colab Notebook for Automaic and Human Evaluation</h2>
A colab notebook is also there in this repo, open than on google colab, upload gold and predicted data, you will get automatic evaluation score. To get human evaluation score collect ratings from humans and pass it as an array. It will calcuate Kohen kappa between two raters, Fleiss' kappa & Krippendorff alpha for all raters.
<a href="https://github.com/human71/comp-mt/blob/main/All_Possible_Text_Evaluation_Methods.ipynb">Run it on: <img src="https://colab.research.google.com/assets/colab-badge.svg" width=8%'></a>
