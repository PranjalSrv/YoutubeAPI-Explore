# YoutubeAPI-Explore
Explore basic information of any YouTube channel and its videos.

Run the dbmaker.py to create a mongo database of the channels' information
  - Modify the variable port to change port of localhost for hosting

  - Add channel names to the list channelnames for the channels whose name is visible in the URL 
  ( eg. https://www.youtube.com/user/DjWalkzz --> Alan Walker, so add 'DjWalkzz' )
  
  - Add channel ID to the list channelids  
  ( eg. https://www.youtube.com/channel/UCG8rbF3g2AMX70yOd8vqIZg --> Logan Paul, so add 'UCG8rbF3g2AMX70yOd8vqIZg' )

Uncomment the lines --statplotting.plottingViews(views)-- in channelstats.py to view graphical representation of views of the previous 10 videos of the channels
