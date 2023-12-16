#!/usr/bin/node
// Searches the second biggest integer in a list of args

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.sort();
  console.log(args.reverse()[1]);
}
