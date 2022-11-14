// SPDX-License-Identifier: GPL-3.0
pragma solidity >= 0.7.0<0.8.0;
contract StudentSystemManagement
{
	struct Student
	{
		int ID;
		string Name;
		int marks;
	}
	address owner;
	int public stdCount = 0;
    mapping(int => Student) public arr;
    event log(string msg);
	constructor()
	{
		owner=msg.sender;
	}
    fallback() external payable {  
         // only 1 in contract , no argument , it is executed when function that does not exists is called , It is mandatory to mark it external.
        emit log("Fallback is called");
    }
	function addNewRecords(int _ID,string memory Name,int marks) public
	{
		stdCount = stdCount + 1;
		arr[stdCount] = Student(_ID,Name, marks);
	}
	function bonusMarks(int _bonus) public
	{
		arr[stdCount].marks = arr[stdCount].marks + _bonus;
	}
}