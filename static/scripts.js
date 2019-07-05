function dosort(i,descending) {
	if(descending)rows.sort(function(a,b){return a[i]<b[i];});
	else rows.sort(function(a,b){return a[i]>b[i];});
	while(t=document.getElementById("datarows")){t.remove();}
	var t = document.getElementById("table");
	console.log(rows.length)
	for(let i = 0; i < rows.length; i++) {
		let r = t.insertRow(-1);
		r.id = "datarows";
		r.align = "center";
		for(let j=0;j<rows[i].length;j++) {
			let c = r.insertCell();
			c.innerHTML = rows[i][j];
		}
	}
}
