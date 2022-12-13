from generation import (
    listGenerator,
    digitsGenerator,
    cpfMask,
)

from validation import ( 
    cpfLength,
    cpfValidator,
    cleanCpf,
    digitsCalc,
    firstDigit,
    secondDigit,
    equalNumbers,
)

def test_firstDigit():
    assert firstDigit('536025396') == 8
    assert firstDigit('592968731') == 2

def test_secondDigit():
    assert secondDigit('536025396') == 1
    assert secondDigit('592968731') == 0

def test_cpfLength():
    assert cpfLength('1919') == False
    assert cpfLength('12345678900') == True
    assert cpfLength('1234567890012') == False

def test_cpfValidator():
    assert cpfValidator('12345678900') == False
    assert cpfValidator('77343717562') == True
    assert cpfValidator('11111111111') == False

def test_listGenerator():
    assert len(listGenerator(5)) == 5

def test_digitsGenerator():
    assert len(digitsGenerator('123452789')) == 2 

def test_cpfMask():
    assert cpfMask('14056110905') == '140.561.109-05'

def test_digitsCalc():
    assert digitsCalc('140561109') == 0
    assert digitsCalc('1405611090') == 5
    assert digitsCalc('132924309') == 9
    assert digitsCalc('1329243099') == 2

def test_digitsCalc():
    assert digitsCalc(233) == 2
    assert digitsCalc(185) == 9
    assert digitsCalc(126) == 5
    assert digitsCalc(153) == 0

def test_equalNumbers():
    assert equalNumbers('12312312323') == False
    assert equalNumbers('11111111111') == True
    assert equalNumbers('2') == True

def test_cleanCpf():
    assert cleanCpf('140.561.109-05') == '14056110905'
    assert cleanCpf('apenasletras2') == '2'
    assert cleanCpf('a.p.s') == ''
    assert cleanCpf('123fdaf4543--.') == '1234543'
