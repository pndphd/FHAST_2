\name{NEWS}
\title{News for Package 'flexclust'}
\section{Changes in flexclust version 1.5-0}{
  \itemize{
    \item The \code{"kccaFamily"} class was modified to also include a
      slot \code{"genDist"} which can be used to define a family where
      its functions, e.g., the distance, depend on the data. This
      contribution was provided by Lena Ortega Menjivar and 
      Dominik Ernst.
    \item The input data for \code{kcca()} can now be an object which
      can be coerced to a numeric matrix using
      \code{\link[base]{data.matrix()}}.
    \item Inserted DOI and removed URL for Leisch (1999).
    \item Packages moved from Depends to Imports.
  }
}    
