$(document).ready(function() { 
    var API_KEY = '5323702';
    var TOKEN = 'moderator_token';
	var recorderManager;
	var recorder;
	var player;
    var archive;
    
    TB.setLogLevel(TB.DEBUG);     
    recorderManager = TB.initRecorderManager(API_KEY);
    
    if (archiveId) {
        player = recorderManager.displayPlayer(archiveId, TOKEN, 'video');
    }
    else {
        recorder = recorderManager.displayRecorder(TOKEN, 'video');
    	recorder.addEventListener('archiveSaved', archiveSavedHandler);        
    }

	function archiveSavedHandler(event) {
	    saveArchive(event.archives[0].archiveId);   
	}

	function saveArchive(archiveId) {
        var movieId = $(':selected').val();
		// Save archiveID to server
		$.ajax({
			url: '/saveArchive/',
			type: 'POST',
			//dataType: 'json',
			data: { "movie_id": movieId, "archive_id": archiveId },
			success: function(data) {
				window.location.href = "/dashboard";
			} 
		});
	}
});


    