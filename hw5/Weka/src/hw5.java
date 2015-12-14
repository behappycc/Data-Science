import weka.core.Instances;
import java.io.BufferedReader;
import java.io.FileReader;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.trees.J48;
import weka.filters.Filter;
import weka.filters.unsupervised.attribute.StringToWordVector;

public class hw5 {
	public static void main(String[] args) throws Exception{
		//parse train and test data
		BufferedReader trainReader = new BufferedReader(new FileReader("ReutersCorn-train.arff"));
		Instances train = new Instances(trainReader);
		train.setClassIndex(train.numAttributes() -1);
		trainReader.close();
		
		BufferedReader testReader = new BufferedReader(new FileReader("ReutersCorn-test.arff"));
		Instances test = new Instances(testReader);
		test.setClassIndex(test.numAttributes() -1);	
		testReader.close();
		
		//filter used to generate word counts
		StringToWordVector filterTrain = new StringToWordVector();
		filterTrain.setInputFormat(train);
		Instances filteredTrainData = Filter.useFilter(train, filterTrain);
		StringToWordVector filterTest = new StringToWordVector();
		filterTest.setInputFormat(test);
		Instances filteredTestData = Filter.useFilter(test, filterTest);
		
		//evaluation
		Evaluation evalJ48 = new Evaluation(filteredTrainData);
		Evaluation evalNaiveBayes = new Evaluation(filteredTrainData);
		
		//Naive Bayes
		NaiveBayes nb = new NaiveBayes();
		nb.buildClassifier(filteredTrainData);
		evalNaiveBayes.evaluateModel(nb, filteredTestData);		
		System.out.println(evalNaiveBayes.toSummaryString("\nNaiveBayes Results\n---------------", false));
		
		//J48
		Classifier cls = new J48();
		cls.buildClassifier(filteredTrainData);
		evalJ48.evaluateModel(cls, filteredTestData);		
		System.out.println(evalJ48.toSummaryString("\nJ48 Results\n---------------", false));		
	}
}

