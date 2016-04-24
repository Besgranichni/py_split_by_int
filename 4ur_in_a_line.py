import os;

clear = lambda: os.system('cls');

class maField_:
	"""docstring for maGame_"""
	def __init__(self):
		self.petope = [];
		self.filler = ' ';

	def setMapSize(self, i, j = 7):	#create map with size i j
		self.petope = [ [ ' ' for __ in range(j) ] for _ in range(i)];

	def getMapSize(self):
		return len(self.petope[0]);

	def setValue(self, i, j, value = None):	#push value in i j cell
		if value == None:
			value = j;
			j = i;
			i = 0;
		self.petope[i][j] = value;

	def getValue(self, i, j):
		return self.petope[i][j];

	def getUpper(self, j):
		for itr in range(len(self.petope)):
			if self.petope[itr][j] != self.filler:
				return itr;

	def replace(self, i, j, ni, nj): #replace i j element to ni nj and fill i j with self.filler
		self.petope[ni][nj] = self.petope[i][j];
		self.petope[i][j] = self.filler;

	def drop(self, j):	#drop down element in j coll if under 'em is a self.filler
		for itr in range(len(self.petope)):
			try:
				if  (self.petope[itr][j] != self.filler) and (self.petope[itr + 1][j] == self.filler):
					self.replace(itr, j, (itr + 1), j);
			except:
				pass

	def printOut(self):	#out map
		for itr in range(len(self.petope)):
			print(self.petope[itr], sep='\n');
			print('-----'*self.getMapSize());

	def checkLines(self, i, j, size, mark = 'auto'):	#check marks repeating with size as a number of steps in a line at x y and z axes
		mark = self.petope[i][j] if mark == 'auto' else ''
		x, y, z = 0, 0, 0;
		for itr in range(size):
			try:
				if ((self.petope[i][j + itr] == mark) or (self.petope[i][j - itr] == mark)) and (j + itr >= 0) : x += 1;
			except:
				pass
			try:
				if ((self.petope[i + itr][j] == mark) or (self.petope[i - itr][j] == mark)) and (i + itr >= 0) : y += 1;
			except:		
				pass
			try:
				if ((self.petope[i + itr][j + itr] == mark) or (self.petope[i + itr][j - itr]) == mark ) : z += 1;
			except:
				pass
			#print('x: ' + str(x) + ' | y: ' + str(y) + ' | z: ' + str(z));
		return True if (x == size) or (y == size) or (z == size) else False;


class maPlayers_:
	def __init__(self, plList, markList = ['x','o','+','-','g']):
		self.plList = plList;
		self.markList = markList;
		self.currPlr = 0;

	def currNum(self):
		return self.currPlr;

	def currName(self):
		return self.plList[self.currPlr];

	def next(self):
		if (self.currPlr < len(self.plList) - 1):
			self.currPlr += 1;
		else:
			self.currPlr = 0;

	def mark(self):
		return self.markList[self.currPlr];


def intInput(text):
	return list(map(lambda x: int(x), input(text).split()));


if __name__ == '__main__':
	
	clear();

	field = maField_();
	i, j = intInput('Размеры игрового поля: ');
	field.setMapSize(i , j);

	pl = maPlayers_(input('Введите игроков: ').split());

	checkSize = 4;
	winner = '';

	field.printOut();

	for itr in range(i * j):
		clear();
		print('\n');
		print( ' ' + pl.currName() + '\'s turn.');
		print('');
		field.printOut();
		print('');
		if (winner != ''):
			break;

		currMot = intInput('###: ')[0] - 1;
		field.setValue(currMot, pl.mark());
		field.drop(currMot);
		if (field.checkLines(field.getUpper(currMot), currMot, checkSize)):
			winner = pl.currName();
		pl.next();



	print('');
	print('Game ended.')
	if winner == '':
		print('Dead heat.');
	else:
		print('Winner is ' + winner + '.');

