# A feature engineering approach for predicting ternary perovskite properties by coupling convolutional neural network with light gradient boosting

Authors: *Ericsson Tetteh Chenebuah, Michel Nganbe and Alain Beaudelaire Tchagang

*Corresponding author: echen013@uottawa.ca

Department of Mechanical Engineering, University of Ottawa, 161 Louis-Pasteur, Ottawa, ON, K1N 6N5 Canada

Digital Technologies Research Centre, National Research Council of Canada, 1200 Montréal Road, Ottawa, ON, K1A 0R6 Canada


# Abstract
In computational theoretical sciences, Machine Learning (ML) techniques are now competitive alternatives that can be used in determining target properties conventionally resolved by ab initio quantum mechanical simulations or experimental synthesization. The successes realized with ML-based techniques often rely on the quality of the design architecture, in addition to the descriptors used in representing a chemical compound with good target mapping property. Building on the Fourier Transformed Crystal Property (FTCP) representation, the present study proposes a new feature engineering approach that takes advantage of both the direct ionic features and the Fourier transformed reciprocal features of a three-dimensional perovskite polyhedral. The study is conducted on about 27,000 ABX3 perovskite structures with the stability energy, the formation energy, and the energy bandgap as targets. For accurate modeling, a two-dimensional convolutional neural network (Conv2D), used primarily to extract high-quality features from the parental descriptor, is coupled with a Light Gradient Boosting Regression (LGBR) machine. A comparison with previous benchmark evaluations reveals appreciable improvements in modeling accuracy for all target properties, particularly for the energy bandgap, for which the feature extraction yields 0.128 eV MAE, 0.320 eV RMSE, and 92.89% R2 based on standardized metrics. Besides, the proposed approach is further demonstrated to out-perform other similar periodic feature engineering approaches in the Coulomb matrix, Ewald-sum matrix, and Sine matrix, all in their absolute eigenvalue forms. In the conclusive aspect, a pixel-importance inspection is carried-out on the Fourier transformed reciprocal space of the high-dimensional (parental) descriptor. From the inspection process, specific crystallographic planes are recognized with good correlation to the target properties, and can potentially be crucial in modeling perovskite’s growth, formation, stability, failure mechanism, and functionality. All data and source codes are made openly available at:  https://github.com/chenebuah/high_dim_descriptor


Keywords: Perovskite, Fourier transformation, Convolutional Neural Network, Light Gradient Boosting, Energy bandgap.



   ![image](https://user-images.githubusercontent.com/74286898/170815967-92672944-89e9-4c33-a973-c083d5c4577f.png)
   
   
This research was supported by the National Science and Engineering Research Council of Canada [NSERC Discovery Grant number: 210487-180599-2001]; and the National Research Council of Canada (NRC) through its Artificial Intelligence for Design Program led by the Digital Technologies Research Centre.
