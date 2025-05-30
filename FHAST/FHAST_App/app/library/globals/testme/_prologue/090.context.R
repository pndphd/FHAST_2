fullTest <- (Sys.getenv("_R_CHECK_FULL_") != "")

covr <- ("covr" %in% loadedNamespaces())
on_macos <- grepl("^darwin", R.version$os)
on_githubactions <- as.logical(Sys.getenv("GITHUB_ACTIONS", "FALSE"))

if (covr) {
  globalenv <- function() parent.frame()
  baseenv <- function() environment(base::sample)
}
