library(shiny)

shinyUI(fluidPage(
  
  titlePanel("Twitter Seniment Analysis"),
  
  sidebarLayout(
    sidebarPanel(
      
      textInput("term","Enter Search Term:","#example"),
      
      sliderInput("i", "Select no. of Tweets:", 0, 1500, 100, step = 50, round = FALSE, format = NULL, locale = NULL, ticks = TRUE, animate = FALSE, width = NULL, sep = ",", pre = NULL, post = NULL, timeFormat = NULL, timezone = NULL, dragRange = TRUE),
      
      
      radioButtons("pType", "Select a Plot type:",
                   list("Sentiment Trends"='a', "Sentiment Scores"='b', "Word Cloud"='c')),
      
      
      
      
      submitButton("Analyze!"),
      
      
      print(h6("  Be Patient, Good Things Take Time!"))
      
      
      
    ),
    
    
    
    # 3D Exploded Pie Chart
library(plotrix)
slices <- c(10, 12, 4, 16, 8) 
lbls <- c("happy", "sad", "angry")
pie3D(slices,labels=lbls,explode=0.1,
   main="Twitter Sentiment Analysis")
    )
  ) )
)
