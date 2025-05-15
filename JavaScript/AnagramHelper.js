function quicksort(array) {
    if (array.length < 2) {
      return array;
    }
  
    let low = [];
    let same = [];
    let high = [];
  
    let pivot = array[Math.floor(Math.random() * array.length)];
  
    for (let item of array) {
      if (item < pivot) {
        low.push(item);
      } else if (item === pivot) {
        same.push(item);
      } else if (item > pivot) {
        high.push(item);
      }
    }
  
    return quicksort(low).concat(same, quicksort(high));
  }
  
  function convert(s) {
    return s.join(" ");
  }
  
  function find_index(elements, value) {
    let index = elements.indexOf(value);
    if (index !== -1) {
      return index;
    }
  }
  
  function anagram_check() {
    let str1 = values[0].toLowerCase();
    let str2 = values[1].toLowerCase();
    if (str1.length === 0) {
      window["-OUT-"].update("Word 1 is empty");
    } else if (str2.length === 0) {
      window["-OUT-"].update("Word 2 is empty");
    } else if (str1.length === str2.length) {
      let sorted_str1 = str1.split("").sort();
      let sorted_str2 = str2.split("").sort();
      if (sorted_str1.join("") === sorted_str2.join("")) {
        window["-OUT-"].update(
          values[0] + " and " + values[1] + " are an anagram"
        );
      } else {
        window["-OUT-"].update(
          values[0] + " and " + values[1] + " are not an anagram"
        );
      }
    } else {
      window["-OUT-"].update(
        values[0] + " and " + values[1] + " are not same length -> not an anagram"
      );
    }
  }
  
  function letter_check() {
    let str1 = values[0].toLowerCase();
    let str2 = values[1].toLowerCase();
    let error = 0;
    let sorted_str1 = str1.split("").sort();
    let sorted_str2 = str2.split("").sort();
    if (sorted_str1.length === sorted_str2.length || sorted_str1.length > sorted_str2.length) {
      for (let i = 0; i < sorted_str2.length; i++) {
        let index = find_index(sorted_str1, sorted_str2[i]);
        if (index !== undefined) {
          sorted_str1.splice(index, 1);
        } else {
          error = 1;
          break;
        }
      }
      let s = convert(sorted_str1);
      if (error === 1) {
        window["-OUT-"].update(
          values[0] + " and " + values[1] + " are not same length -> not an anagram"
        );
        window["-LET-"].update("1 letter used too much: " + sorted_str2[i]);
      } else if (error === 0) {
        if (s.length === 0) {
          window["-LET-"].update("All letters used");
          anagram_check();
        } else {
          window["-OUT-"].update(
            values[0] + " and " + values[1] + " are not same length -> not an anagram"
          );
          window["-LET-"].update("Still available characters: " + s);
        }
      }
    } else {
      window["-OUT-"].update(
        values[0] + " and " + values[1] + " are not same length -> not an anagram"
      );
      window["-LET-"].update("Too many characters in 2nd word");
    }
  }
  
  function random_perms() {
    let str1 = values[0].toLowerCase();
    if (str1.length < 7) {
      window["-PERM-"].update(sorted(Array.from(perms)));
    } else {
      let k = 200;
      let permsl = Array.from(perms).sort(() => Math.random() - 0.5).slice(0, k);
      let permssort = quicksort(permsl);
      window["-PERM-"].update(permssort);
    }
  }
  
  function run_once(f) {
    function wrapper(...args) {
      if (wrapper.has_run !== values[0].toLowerCase()) {
        wrapper.has_run = values[0].toLowerCase();
        return f(...args);
      } else {
        random_perms();
      }
    }
    wrapper.has_run = "";
    return wrapper;
  }
  
  function create_perm() {
    let str1 = values[0].toLowerCase();
    perms = new Set(Array.from(permutations(str1)).map((x) => x.join("")));
    random_perms();
  }
  
  let default_theme = "DarkBlue";
  let perms = new Set();
  
  let layout = [
    [sg.Text("Please enter 2 Words")],
    [sg.Text("Word 1"), sg.InputText()],
    [sg.Text("Word 2"), sg.InputText()],
    [sg.Text({ auto_size_text: true, key: "-OUT-" })],
    [sg.Text({ auto_size_text: true, key: "-LET-" })],
    [sg.Multiline({ key: "-PERM-", size: [70, 10] })],
    [
      sg.Button("Anagram"),
      sg.Button("Letters"),
      sg.Button("Create Permutation", { tooltip: "Creates permutations of Word 1" }),
      sg.Button("Exit"),
    ],
  ];
  
  let window = sg.Window("Anagram Name Helper", layout);
  while (true) {
    let event, values;
    try {
      let result = window.read();
      event = result[0];
      values = result[1];
    } catch (err) {
      break;
    }
    if (event === sg.WIN_CLOSED || event === "Exit") {
      break;
    } else if (event === "Anagram") {
      anagram_check();
    } else if (event === "Letters") {
      letter_check();
    } else if (event === "Create Permutation") {
      create_perm();
    }
  }
  window.close();