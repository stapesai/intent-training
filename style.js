var slider = document.getElementById("column-slider");
var leftColumn = document.getElementById("left-column");
var rightColumn = document.getElementById("right-column");

slider.oninput = function() {
  leftColumn.style.flex = this.value / 100;
  rightColumn.style.flex = (100 - this.value) / 100;
}