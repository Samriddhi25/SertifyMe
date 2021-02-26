<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name:"app",
  components: {}
}
</script>


<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Poppins, Helvetica, sans-serif;
    line-height: 1.4;
    overflow-x: hidden;
  }

  .btn {
    display: inline-block;
    border: none;
    background: #0d1413;
    color: #4A8280;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover {
    background: #284140;
  }
	::-webkit-scrollbar {
		width: 10px;
		border: 0;
		height: 5px;
	}
	::-webkit-scrollbar-track {
		background: transparent;
	}
	::-webkit-scrollbar-thumb {
		background: #284140;
	}
	::-webkit-scrollbar-thumb:hover {
		background: #4A8280;
	}

</style>
