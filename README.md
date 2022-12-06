# A Fourier-transformed feature engineering design for predicting ternary perovskite properties by coupling a two-dimensional convolutional neural network with a support vector machine (Conv2D-SVM)

Authors: *Ericsson Tetteh Chenebuah, Michel Nganbe and Alain Beaudelaire Tchagang

*Corresponding author: echen013@uottawa.ca

Department of Mechanical Engineering, University of Ottawa, 161 Louis-Pasteur, Ottawa, ON, K1N 6N5 Canada

Digital Technologies Research Centre, National Research Council of Canada, 1200 Montréal Road, Ottawa, ON, K1A 0R6 Canada


# Abstract
In computational material sciences, Machine Learning (ML) techniques are now competitive alternatives that can be used in determining target properties conventionally resolved by ab initio quantum mechanical simulations or experimental synthesization. The successes realized with ML-based techniques often rely on the quality of the design architecture, in addition to the descriptors used in representing a chemical compound with good target mapping property. With the perovskite crystal structure at the forefront of modern energy materials discovery, accurately estimating related target properties is even of high importance due to the role such properties may have in defining the functionalization. As a result, the present study proposes a new feature engineering approach that takes advantage of both the direct ionic features and the periodic Fourier transformed reciprocal features of a three-dimensional perovskite polyhedral. The study is conducted on about 27,000 ABX3 perovskite structures with the stability energy, the formation energy, and the energy bandgap as targets. For accurate modeling, a feature-extracting two-dimensional convolutional neural network (Conv2D) is coupled with a prediction-enhancing Support Vector Machine (SVM) to form a hybridized Conv2D-SVM architecture. A comparison with previous benchmark evaluations reveals appreciable improvements in modeling accuracy for all target properties, particularly for the energy bandgap, for which the feature extraction approach yields 0.105 eV MAE, 0.301 eV RMSE, and 93.48% R2. Besides, the proposed design is further demonstrated to out-perform other similar periodic feature engineering approaches in the Coulomb matrix, Ewald-sum matrix, and Sine matrix, all in their absolute eigenvalue forms. All preprocessed data, source codes, and relevant sample calculations are openly available at: github.com/chenebuah/high_dim_descriptor


Keywords: Perovskite, Fourier transformation, Convolutional Neural Network, Support vector Machine, Energy bandgap.



   ![image](https://user-images.githubusercontent.com/74286898/170815967-92672944-89e9-4c33-a973-c083d5c4577f.png)
   
   
This research was supported by the National Science and Engineering Research Council of Canada [NSERC Discovery Grant number: 210487-180599-2001]; and the National Research Council of Canada (NRC) through its Artificial Intelligence for Design Program led by the Digital Technologies Research Centre.
