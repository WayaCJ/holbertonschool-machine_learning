For a node 
 containing a population 
 that is partitioned in 
 classes : 
 , the Gini impurity of 
 is defined as

 
 

The idea behind this definition is that

if the population of a node is equally partitioned into many classes, the Gini impurity will be large
if the population of a node comes mainly from one class, the Gini impurity will be small
So

if the Gini impurity of a leaf is large, we cannot be very confident in the prediction function of this node
if the Gini impurity of a leaf is small, we can have more confidence in the prediction function of this node
Hence the idea to split a node is to choose the feature and the threshold for which the average of the Gini impurities of the corresponding children is the smallest.

 
 

Task: To find this value :

Update the the Decision_Tree class by adding the new methods down below.
Fill in the gap in the method def Gini_split_criterion_one_feature(self,node,feature) :.
No for or while loop allowed !
def possible_thresholds(self,node,feature) :
        values = np.unique((self.explanatory[:,feature])[node.sub_population])
        return (values[1:]+values[:-1])/2

def Gini_split_criterion_one_feature(self,node,feature) :
        # Compute a numpy array of booleans Left_F of shape (n,t,c) where
        #    -> n is the number of individuals in the sub_population corresponding to node
        #    -> t is the number of possible thresholds
        #    -> c is the number of classes represented in node
        # such that Left_F[ i , j , k] is true iff 
        #    -> the i-th individual in node is of class k 
        #    -> the value of the chosen feature on the i-th individual 
        #                              is greater than the t-th possible threshold
        # then by squaring and summing along 2 of the axes of Left_F[ i , j , k], 
        #                     you can get the Gini impurities of the putative left childs
        #                    as a 1D numpy array of size t 
        #
        # Then do the same with the right child
        # Then compute the average sum of these Gini impurities
        #
        # Then  return the threshold and the Gini average  for which the Gini average is the smallest

        def Gini_split_criterion(self,node):
                X=np.array([self.Gini_split_criterion_one_feature(node,i) for i in range(self.explanatory.shape[1])])
                i =np.argmin(X[:,1])
                return i, X[i,0]
