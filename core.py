# code based for UCSD Machine Learning project for spectral binaries
# -*- coding: utf-8 -*-
from __future__ import print_function


VERSION = '2023.01.16'
__version__ = VERSION
GITHUB_URL = 'https://github.com/Ultracool-Machine-Learning/spectral_binaries'
CODE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = CODE_PATH+'/data/'
ERROR_CHECKING = False


######################################################
#######################################################
###############   DISPLAY ON LOAD IN  #################
#######################################################
#######################################################

print('\n\nWelcome to the UCSD Machine Learning Project Spectral Binary Code!')
print('You are currently using version {}\n'.format(VERSION))
# print('If you make use of any features of this toolkit for your research, please remember to cite the paper:')
# print('\n{}; Bibcode: {}\n'.format(CITATION,BIBCODE))
print('Please report any errors are feature requests to our github page, {}\n\n'.format(GITHUB_URL))


#######################################################
########## BASIC SPECTRAL ANALYSIS FUNCTIONS ##########
#######################################################

def measureSN(wave, flux, unc, rng=[1.2,1.35]):
	"""
	Measures the signal to noise of a spectrum over a specified wavelength range

	Parameters
	----------
	wave : list or numpy array of floats
			An array specifying wavelength in units of microns
			
	flux : list or numpy array of floats
			An array specifying flux density in f_lambda units
			
	unc : list or numpy array of floats
			An array specifying uncertainty in the same units as flux
			
	rng : 2-element list of floats, default = [1.2,1.35]
			Specifies the range over which S/N is measured

	Returns
	-------
	float
		Median signal-to-noise value in the specified range

	Examples
	--------
	>>> wave = np.linspace(1,3,100)
	>>> flux = np.random.normal(5,0.2,100)
	>>> unc = flux*0.01
	>>> measureSN(wave,flux,unc)
	0.01

	"""

	pass



def classify(wave, flux, unc, method='kirkpatrick'):
	"""
	Measures the classification of a spectrum against a set of standards using predefined methods

	Parameters
	----------
	wave : list or numpy array of floats
			An array specifying wavelength in units of microns
			
	flux : list or numpy array of floats
			An array specifying flux density in f_lambda units
			
	unc : list or numpy array of floats
			An array specifying uncertainty in the same units as flux
			
	nethod : str, default='kirkpatrick'
			Specifies the method of classification; values may include:
			* 'kirkpatrick': compare to spectral standards over the 0.9 to 1.4 µm range
			* 'fast': use fastclassify method (?)

	Returns
	-------
	float
		Numerical spectral type of classification, with 15 = M5, 25 = L5, 35 = T5, etc

	Examples
	--------
	>>> wave = np.linspace(1,3,100)
	>>> flux = np.random.normal(5,0.2,100)
	>>> unc = flux*0.01
	>>> classify(wave,flux,unc)
	0.01

	"""

	pass



def normalize(wave, flux, unc, rng=[1.2,1.35], method='median'):
	"""
	Normalizes the spectrum of an object over a given wavelength range

	Parameters
	----------
	wave : list or numpy array of floats
			An array specifying wavelength in units of microns
			
	flux : list or numpy array of floats
			An array specifying flux density in f_lambda units
			
	unc : list or numpy array of floats
			An array specifying uncertainty in the same units as flux
			
	rng : 2-element list of floats, default = [1.2,1.35]
			Specifies the range over which normalization is computed

	method : str, default = 'median'
			Specifies the method by which normalization is determined; options are:
			* 'median': compute the median value within rng
			* 'max': compute the maximum value within rng

	Returns
	-------
	list or numpy array of floats
		normalized flux

	list or numpy array of floats
		normalized uncertainty

	Examples
	--------
	>>> wave = np.linspace(1,3,100)
	>>> flux = np.random.normal(5,0.2,100)
	>>> unc = flux*0.01
	>>> nflux, nunc = normalize(wave,flux,unc)

	"""

	pass


def addNoise(wave, flux, unc, scale=1.):
	"""
	Resamples data to add noise, scaled according to input scale factor (scale > 1 => increased noise)

	Parameters
	----------
	wave : list or numpy array of floats
			An array specifying wavelength in units of microns
			
	flux : list or numpy array of floats
			An array specifying flux density in f_lambda units
			
	unc : list or numpy array of floats
			An array specifying uncertainty in the same units as flux
			
	scale : float, default = 1.
			Scale factor to scale uncertainty array; scale > 1 reduces signal-to-noise

	Returns
	-------
	list or numpy array of floats
		flux with noise added

	list or numpy array of floats
		scaled uncertainty

	Examples
	--------
	>>> wave = np.linspace(1,3,100)
	>>> flux = np.random.normal(5,0.2,100)
	>>> unc = flux*0.01
	>>> nflux, nunc = addNoise(wave,flux,unc,scale=5.)

	"""

	pass


def readTemplates(file='single_spectra.h5'):
	"""
	Reads in single templates, contained in data folder and stored in h5 format

	Parameters
	----------
	file : str, default = 'single_spectra.h5'
			file to read in, defaulting to based single templates in data folder

	Returns
	-------
	numpy array of floats
		wavelength scale

	pandas.DataFrame
		pandas table containing fluxes, uncertainties, and additional information 


	Examples
	--------
	>>> wave, tbl = readTemplates()

	"""

	pass


def makeRFClassifyTraining(wave,templates,sample_definitions={},oversample=True,overtotal=-1,balanced=True,uniformSN=True):
	"""
	Builds trainig sample from singles based on defined inputs

	Parameters
	----------
	wave : list or numpy array of floats
			An array specifying wavelength in units of microns

	templates : pandas.DataFrame
			pandas table containing fluxes, uncertainties, and additional information

	sample_definitions : dict, default = {}
			parameters that define how training sample is constructed;
			by default, all pairs with secondary spectral type >= primary spectral type are constucted
			specifications can be as follows:
			* 'select_single' : 2-element array of floats specifying minimum and maximum spectral type of singles
			* 'select_primary' : 2-element array of floats specifying minimum and maximum spectral type of primaries
			* 'select_secondary' : 2-element array of floats specifying minimum and maximum spectral type of secondaries
			* 'select_combined' : 2-element array of floats specifying minimum and maximum spectral type of combined binaries
			* 'select_snr' : 2-element array of floats specifying minimum and maximum signal-to-noise values of all spectra
			* 'include_difference' : bool, if True computes the difference spectra between template and best fit standard and includes in labels 
			* 'normalize_range' : 2-element array of floats specifying wavelength range for normalization
			* 'normalize_method' : str specifying method of normalization
			* 'sn_range' : 2-element array of floats specifying wavelength range for signal-to-noise computation
			* 'classify_method' : str specifying method of normalization

	balance : bool, default = True
			enforce balance 

	oversample : bool, default = True
			acheive single/binary balance by oversampling dataset through addNoise()
			if False, will reduce either single or binary sample to acheive balance

	overnumber : int, default = -1
			target value for single and binary samples for balanced oversampling
			if less than maximum number of either single or binary samples, will balance to the larger sample size
			
	uniformSN : bool, default = True
			if oversampling, enforce uniform distributions of signal-to-noise in single and binary samples


	Returns
	-------
	pandas.DataFrame
		pandas table containing training sample labels and classifications for input to random forest classifier


	Examples
	--------
	>>> wave, tbl = readTemplates()
	>>> trainset = makeRFClassifyTraining(wave,tbl,oversample=True,overnumber=10000,uniformSN=True)

	"""

# verify single templates

# downselect single templates based on criteria

# make binaries

# downselect binaries based on criteria

# add in additional labels based on criteria

# resample with addNoise() if balance and oversample are requested, 
# checking SN is uniformSN is True

# clean up output table and return

	pass


def trainRFClassify(templates,model_parameters={},verbose=True,plot=True,plotfilebase=''):
	"""
	Trains a random forest model based on training sample, returns model parameters and output statistics

	Parameters
	----------
	templates : pandas.DataFrame
			pandas table containing training set with all relevant labels and classifications

	model_parameters : dict, default = {}
			parameters that define how random forest model is constructed
			specifications can be as follows:
			* 'n_trees' : int, default = 50
			* 'train_test_split' : 2-element array of floats specifying fraction of templates used for training and testing, default = [0.75,0.25]
			* 'hyperparameter_optimize' : bool, default = False
			* OTHERS?
			
	verbose : bool, default = True
			provide verbose feedback as train is undergoing, including report of statistics 

	plot : bool, default = True
			produce diagnostic plots of outcomes, including confusion matrix and feature importance

	plotfilebase : str, deafult = ''
			base path string to save plot files, to which '_confusion-matrix.pdf' and '_feature-importance.pdf' are appended
			if equal to '', plots are displayed to screen only

	Returns
	-------
	dict
		dictionary containing model parameters and analysis statistics


	Examples
	--------
	>>> wave, tbl = readTemplates()
	>>> trainset = makeRFClassifyTraining(wave,tbl,oversample=True,overnumber=10000,uniformSN=True)
	>>> results = trainRFClassify(tbl,plot=True,plotfilebase='/Users/adam/ML/test')

	"""

# build RF model based on parameters

# conduct training and testing

# report statistics

# generate diagnostic plots

# return model parameters

	pass


def RFclassify(parameters,labels,verbose=True):
	"""
	Uses a pre-trained random forest model to classify a spectrum

	Parameters
	----------
	parameters : ???
			random forest model parameters

	labels : list and numpy array of floats
			labels to conduct classification; must be same dimension as training labels

	verbose : bool, default = True
			provide verbose feedback as train is undergoing, including report of statistics 

	Returns
	-------
	tuple
		classification value (0 or 1) and percentage of trees that made that classification (reliability)


	Examples
	--------
	>>> wave, tbl = readTemplates()
	>>> trainset = makeRFClassifyTraining(wave,tbl,oversample=True,overnumber=10000,uniformSN=True)
	>>> results = trainRFClassify(tbl,plot=True,plotfilebase='/Users/adam/ML/test')

	"""

# check inputs

# compute classification and output

	pass









