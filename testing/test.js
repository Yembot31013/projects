// define a function
function printcard(){
  line1="<strong>name:</strong>" + this.name + "<br/>\n";
  line2="<strong>address:</strong>" + this.address + "<br/>\n";
  line3="<strong>work:</strong>" + this.work + "<br/>\n";
  line4="<strong>home:</strong>" + this.home + "<br/>\n";
  Document.write(line1,line2,line3,line4);
}
function card(name,address,work,home){
  this.name=name;
  this.address=address;
  this.work=work;
  this.work=work;
  this.printcard=printcard;
}
// create the object
sue=('sue suther','523 elm street','555-1234','555-9876');
afred=('afred suther','124 ishage street','555-1235','555-9873');
heric=('heric suther','23 abule street','555-1236','555-9874');
anna=('anna suther','133 yes street','555-1235','555-9875');
// print them
sue.printcard();
afred.printcard();
heric.printcard();
anna.printcard();
