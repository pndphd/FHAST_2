library(globals)

options(warn = 2L)

exprs <- list(
  ok1   = quote(function(...) sum(x, ...)),
  ok2   = quote(function(...) sum(x, ..1, ..2, ..3)),
  warn1 = quote(sum(x, ...)),
  warn2 = quote(sum(x, ..1, ..2, ..3))
)

truth <- list(
  ok1 = c("sum", "x"),
  ok2 = c("sum", "x"),
  warn1 = c("sum", "x", "..."),
  warn2 = c("sum", "x", "..1", "..2", "..3")
)

message("*** findGlobals() ...")

for (name in names(exprs)) {
  expr <- exprs[[name]]

  message(sprintf("\n*** codetools::findGlobals() - step %s:", sQuote(name)))
  print(expr)
  fun <- globals:::as_function(expr)
  print(fun)
  ## Suppress '... may be used in an incorrect context' warnings
  suppressWarnings({
    globals <- codetools::findGlobals(fun)
  })
  print(globals)
  assert_identical_sets(globals, c("sum", "x"))
  next
  
  message("\n*** findGlobals(dotdotdot = 'ignore'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)  
  globals <- findGlobals(expr, dotdotdot = "ignore")
  print(globals)
  assert_identical_sets(globals, c("sum", "x"))

  message("\n*** findGlobals(dotdotdot = 'return'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- findGlobals(expr, dotdotdot = "return")
  print(globals)
  assert_identical_sets(globals, truth[[name]])

  message("\n*** findGlobals(dotdotdot = 'warning'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- findGlobals(expr, dotdotdot = "warning")
  print(globals)
  assert_identical_sets(globals, truth[[name]])

  message("\n*** findGlobals(dotdotdot = 'error'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- tryCatch(findGlobals(expr, dotdotdot = "error"), error = identity)
  if (name %in% c("ok1", "ok2")) {
    assert_identical_sets(globals, truth[[name]])
  } else {
    stopifnot(inherits(globals, "error"))
  }
} # for (name ...)


message("\n*** findGlobals(<exprs>, dotdotdot = 'return'):")
print(exprs)
globals <- findGlobals(exprs, dotdotdot = "return")
print(globals)
assert_identical_sets(globals, unique(unlist(truth, use.names = FALSE)))

message("\n*** findGlobals(<attribute-with-formula-and-dots>, dotdotdot = 'return'):")
formula_attr <- bquote(~ .(call("fn", quote(...))))
x <- structure(integer(), formula_attr = formula_attr)
print(x)
# Attributes always use `dotdotdot = "ignore"`
globals <- findGlobals(x, dotdotdot = "return", attributes = TRUE)
print(globals)
assert_identical_sets(globals, c("~", "fn"))

message("*** findGlobals() ... DONE")



message("*** globalsOf() ...")

x <- 1:2

for (name in names(exprs)) {
  expr <- exprs[[name]]

  message("\n*** globalsOf(dotdotdot = 'ignore'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "ignore")
  print(globals)
  assert_identical_sets(names(globals), c("sum", "x"))
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'return'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "return")
  print(globals)
  assert_identical_sets(names(globals), truth[[name]])
  if (name == "warn1") {
    stopifnot(!is.list(globals$`...`) && is.na(globals$`...`))
  }
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'warning'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "warning")
  print(globals)
  assert_identical_sets(names(globals), truth[[name]])
  if (name == "warn1") {
    stopifnot(!is.list(globals$`...`) && is.na(globals$`...`))
  }
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'error'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- tryCatch(globalsOf(expr, dotdotdot = "error"), error = identity)
  if (name %in% c("ok1", "ok2")) {
    assert_identical_sets(names(globals), truth[[name]])
    stopifnot(all.equal(globals$sum, base::sum))
    stopifnot(all.equal(globals$x, x))
  } else {
    stopifnot(inherits(globals, "error"))
  }
} # for (name ...)

message("\n*** globalsOf(<exprs>, dotdotdot = 'return'):")
print(exprs)
globals <- globalsOf(exprs, dotdotdot = "return")
print(globals)


message("*** globalsOf() ... DONE")


message("*** function(x, ...) globalsOf() ...")

aux <- function(x, ..., exprs) {
  args <- list(...)

for (name in names(exprs)) {
  expr <- exprs[[name]]

  message("\n*** globalsOf(dotdotdot = 'ignore'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "ignore")
  print(globals)
  assert_identical_sets(names(globals), c("sum", "x"))
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'return'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "return")
  print(globals)
  assert_identical_sets(names(globals), truth[[name]])
  if (name == "warn1") {
    stopifnot(all.equal(globals$`...`, args, check.attributes = FALSE))
  }
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'warning'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- globalsOf(expr, dotdotdot = "warning")
  print(globals)
  assert_identical_sets(names(globals), truth[[name]])
  if (name == "warn1") {
    stopifnot(all.equal(globals$`...`, args, check.attributes = FALSE))
  }
  stopifnot(all.equal(globals$sum, base::sum))
  stopifnot(all.equal(globals$x, x))

  message("\n*** globalsOf(dotdotdot = 'error'):")
  cat(sprintf("Expression '%s':\n", name))
  print(expr)
  globals <- tryCatch(globalsOf(expr, dotdotdot = "error"), error = identity)
  if (name %in% c("ok1", "ok2")) {
    assert_identical_sets(names(globals), truth[[name]])
    stopifnot(all.equal(globals$sum, base::sum))
    stopifnot(all.equal(globals$x, x))
  } else {
    stopifnot(inherits(globals, "error"))
  }
} # for (name ...)

message("\n*** globalsOf(<exprs>, dotdotdot = 'return'):")
print(exprs)
globals <- globalsOf(exprs, dotdotdot = "return")
print(globals)

} # aux()

aux(x = 3:4, y = 1, z = 42L, 3.14, exprs = exprs)
message("*** function(x, ...) globalsOf() ... DONE")


## Cleanup
