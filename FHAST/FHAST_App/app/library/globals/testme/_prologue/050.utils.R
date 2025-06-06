assert_identical_sets <- function(a, b) {
  a <- sort(a)
  b <- sort(b)
  if (!identical(a, b)) {
    stop(sprintf("Non-identical sets: %s != %s",
         paste(sQuote(a), collapse = ", "),
         paste(sQuote(b), collapse = ", ")))
  }
}
