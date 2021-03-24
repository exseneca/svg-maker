

let thumb = document.getElementById('slidecursor');
let threshold = 0;

thumb.onmousedown = function(event) {
  event.preventDefault(); // prevent selection start (browser action)

  let shiftX = event.clientX - thumb.getBoundingClientRect().left;
  // shiftY not needed, the thumb moves only horizontally

  document.addEventListener('mousemove', onMouseMove);
  document.addEventListener('mouseup', onMouseUp);

  function onMouseMove(event) {
    let newLeft = event.clientX - shiftX - slider.getBoundingClientRect().left;

    // the pointer is out of slider => lock the thumb within the bounaries
    if (newLeft < 0) {
      newLeft = 0;
    }
    let rightEdge = slider.offsetWidth - thumb.offsetWidth;
    if (newLeft > rightEdge) {
      newLeft = rightEdge;
    }
    let sliderWidth = slider.offsetWidth;
    let percentageAcross = (newLeft/sliderWidth).toPrecision(5);
    threshold = Math.floor(255*percentageAcross);
    let after_image = document.getElementById('img2');
    after_image.src = after_image.src.split('threshold')[0] + 'threshold-' + threshold.toString() + '.jpg';


    thumb.style.left = newLeft + 'px';
  }

  function onMouseUp() {
    document.removeEventListener('mouseup', onMouseUp);
    document.removeEventListener('mousemove', onMouseMove);
  }

};

thumb.ondragstart = function() {
  return false;
};