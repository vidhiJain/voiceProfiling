library(tuneR)
library(seewave)
fs <- list.files(path = getwd(), pattern = ".wav$", ignore.case = TRUE)
for(i in fs){
  print(i)
}
# convert if any mp3 to wav
for (item in fs){
  #audio_mp3 <- readMP3(item)
  #file_name <- substr(item, 1, nchar(item)-4)
  #audio_wav_path <- paste(file_name, "wav", sep = ".")
  #writeWave(audio_mp3,audio_wav_path,extensible=FALSE)
  r <- tuneR::readWave(item)
  #frequency spectrum analysis
  songspec <- seewave::spec(r, f = r@samp.rate, plot = TRUE)
  analysis <- seewave::specprop(songspec, f = r@samp.rate, flim = c(0, 280/1000), plot = TRUE)
  
  #save parameters
  meanfreq <- analysis$mean/1000
  sd <- analysis$sd/1000
  median <- analysis$median/1000
  Q25 <- analysis$Q25/1000
  Q75 <- analysis$Q75/1000
  IQR <- analysis$IQR/1000
  skew <- analysis$skewness
  kurt <- analysis$kurtosis
  sp.ent <- analysis$sh
  sfm <- analysis$sfm
  mode <- analysis$mode/1000
  centroid <- analysis$cent/1000
  bp <- c(0, 22)
  b <- bp
  if (b[2]>ceiling(r@samp.rate/2000)-1)
	b[2] <- ceiling(r@samp.rate/2000)-1
  y<-seewave::dfreq(r, f = r@samp.rate, wl = 2048, ylim =c(0,280/1000), ovlp = 0, plot = FALSE, threshold = 5, bandpass = b *1000, fftw =TRUE) [, 2]
  meandom <- mean(y, na.rm  = TRUE)
  mindom<- min(y, na.rm = TRUE)
  maxdom <- max(y, na.rm =TRUE)
  dfrange <- (maxdom - mindom)
  
  #Fundamental frequency parameters
  ff <- seewave::fund(r, f = r@samp.rate, ovlp = 50, threshold = 5, fmax = 280, ylim=c(0, 280/1000), plot = FALSE, wl = 2048)[, 2]
  meanfun<-mean(ff, na.rm = T)
  minfun<-min(ff, na.rm = T)
  maxfun<-max(ff, na.rm = T)
  
  #modulation index calculation
  changes <- vector()
  for(j in which(!is.na(y))){
  	change <- abs(y[j] - y[j + 1])
  	changes <- append(changes, change)
  }
  if(mindom==maxdom) modindx<-0 else modindx <- mean(changes, na.rm = T)/dfrange
  
  duration <- seewave::duration(r, f)
  
  #save results
  array <- data.frame(item, duration,meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, sp.ent, sfm, mode, centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx)
  
  write.table(array, file = "attributes.csv", sep = ",", append=TRUE, row.names = FALSE, col.names = FALSE)

}

