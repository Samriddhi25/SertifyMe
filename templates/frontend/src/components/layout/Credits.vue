<template>
  <div class="footer-holder">
    <div class="footer-data">
      <h2>SertifyMe <span>© 2021</span></h2>
      <div class="footer-info">
        <p>
          SertifyMe is a Web application which provides a simple solution to the
          tedious task of publishing and distributing e-certificates.
        </p>
      </div>
      <div class="footer-owner">
        <div class="footer-owner-info">
          <h5>
            <a href="http://www.linkedin.com/in/samriddhiagarwal25"
              >Samriddhi Agarwal</a
            >
          </h5>
          <h5>
            <a href="mailto:samriddhiagarwal12@gmail.com"
              >samriddhiagarwal12@gmail.com</a
            >
          </h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.footer-holder {
  width: 100vw;
  background: #243734;
  color: aliceblue;
  text-align: center;
  padding: 20px;
}
.footer-data {
  padding-left: 20%;
  width: 80%;
}
.footer-info {
  color: #4A8280;
  margin: 20px;
}
.footer-owner-info {
  display: flex;
  justify-content: space-evenly;
  margin-bottom: 10px;
}
a {
  color: #e7efee;
  text-decoration: none;
  margin: 10px;
}
h5 :hover {
  color: #8ec2bb;
}
span {
  font-size: 12px;
}
</style>