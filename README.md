# A feature engineering approach for modeling ternary perovskite target properties by Fourier transforming direct features into the periodic reciprocal crystal lattice

Authors: *Ericsson Tetteh Chenebuah, Michel Nganbe and Alain Beaudelaire Tchagang

*Corresponding author: echen013@uottawa.ca
Department of Mechanical Engineering, University of Ottawa, 161 Louis-Pasteur, Ottawa, ON, K1N 6N5 Canada


# Abstract
In computational theoretical sciences, Machine Learning (ML) techniques are now competitive alternatives that can be used in determining target properties conventionally resolved by ab initio quantum mechanical simulations or experimental synthesization. The successes realized with ML-based techniques often rely on the quality of the design architecture, in addition to the descriptors used in representing a chemical compound with good target mapping property. In the present study, a novel feature engineering approach is developed, which explores the reciprocal lattice space of a periodic crystal structure. The ML experiment is conducted on about 27,000 ABX3 perovskite structures with target objective on the accurate modeling of the stability energy, formation energy, and energy band gap. The descriptor used to represent a sample takes advantage of both the direct ionic features and the Fourier-transformed reciprocal features that are associated with a three-dimensional perovskite polyhedral. For accurate target modeling, a deep convolutional neural network (Conv2D), used primarily to extract high-quality features from the parental descriptor, is coupled with a Light Gradient Boosting Regression (LGBR) machine. The obtained results reveal appreciable improvements in modeling accuracy for all considered target properties. For the energy band gap in particular, the feature extraction approach works remarkably well at 0.128 eV MAE, 0.320 eV RMSE, and 92.89% R2 on standardized metrics, exceeding previous benchmark expectations. Besides, the proposed approach is further demonstrated to out-perform other similar periodic descriptors in the Coulomb matrix, Ewald-sum matrix, and Sine matrix, all in their absolute eigenvalue forms. In the conclusive aspect of this work, a pixel-importance inspection is carried-out on the Fourier-transformed reciprocal space of the high-dimensional descriptor. From the inspection process, specific crystallographic planes are recognized with good correlation to the target properties, and can potentially be crucial in modeling perovskite’s growth, formation, stability, failure mechanism, and functionality.


Keywords: Perovskite, Fourier transformation, Reciprocal crystal lattice, Energy band gap, Machine Learning



   ![image](https://user-images.githubusercontent.com/74286898/170815967-92672944-89e9-4c33-a973-c083d5c4577f.png)
