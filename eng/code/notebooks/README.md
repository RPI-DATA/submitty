# Lecture 3 in-class: Matrix-vector product and Numpy I/O

Students are assessed on their ability to read and write data in .npy format,
and use this data to compute a matrix-vector product.  Their resulting product
is compared, entrywise, against an expected result.  The entries are
considered correct if they agree to within a specified tolerance.

The matrix and vector for the product are stored in `matrix.npy` and `vector.npy`, respectively.  The students must write their product to a file named `result.npy`; failure to do so will result in a `FileNotFoundError`.

After running the student's script, Submitty runs the `check` script, which does the necessary floating-point comparison.  The `check` script prints to stdout, and only if this output matches `test_output/check_output.txt` is the product considered accurate.

In addition to accuracy, Submitty checks the following:

* the use of an `import` statement
* the presence of two `for` loops
* the presence of `+=`
