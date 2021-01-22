<template>
  <main-layout>
    <div class="create-certificate">
      <div class="steps">
        <div
          class="choose"
          v-bind:class="{ active: check == 1 }"
          v-on:click="updateStep(1)"
        >
          Choose a template for you !
        </div>
        <div class="crumps"></div>
        <div
          class="choose"
          v-bind:class="{ active: check == 2 }"
          v-on:click="updateStep(2)"
        >
          Input data for the certificate 😄
        </div>
        <div class="crumps"></div>
        <div
          class="choose"
          v-bind:class="{ active: check == 3 }"
          v-on:click="updateStep(3)"
        >
          Want us to send them emails ?
        </div>
      </div>
      <div class="comp">
        <div class="show-temp" v-if="check == 1">
          <div class="head">
            <div v-if="checkProps == 0">
              <router-link :to="{ name: 'template' }" class="certy-btn">
                Choose Template
              </router-link>
            </div>
            <div v-else>Your have Selected the following Template</div>
          </div>
          <div class="temp">
            <div v-if="checkProps == 0" class="temp-image">
              <img src="../assets/noImage.jpg" class="certi_image" />
            </div>
            <div v-else class="temp-image">
              <img
                :src="getImgUrl(tempID)"
                v-bind:alt="tempID"
                class="certi_image"
              />
            </div>
          </div>
        </div>
        <div class="show-text" v-if="check == 2">
          <div class="head">Please Select your data Sheet ( .xlsx )</div>
          <div class="temp drop">
            <input type="file" @change="onFileChange" />
          </div>
          <div class="head">Enter Speaker Name (1)</div>
          <div class="temp input">
            <input v-model="speaker1" placeholder="Enter name" />
          </div>
          <div class="head">Enter Speaker Name (2)</div>
          <div class="temp input">
            <input v-model="speaker2" placeholder="Enter name" />
          </div>
          <div class="button">
            <button class="certy-btn confirm" v-on:click="submit()">
              Confirm
            </button>
          </div>
        </div>
        <div class="show-email" v-if="check == 3">
          <div class="head">
            We have Successfuly made Local copy of All the certificates for You
            !!
          </div>
          <div class="temp">
            <div class="contain">
              <div class="vertical-center">
                <div class="service">
                  Would You like to use our Email service ?
                </div>
                <div class="button">
                  <button class="certy-btn confirm" v-on:click="email(true)">
                    Yes
                  </button>
                  <div v-on:click="email(false)" class="noemail">No</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main-layout>
</template>

<script>
import MainLayout from "../components/layout/Main";
import axios from 'axios';

export default {
  components: {
    MainLayout,
  },
  data() {
    return {
      steps: 1,
      tempID:
        this.$route.params.certiID === undefined
          ? 0
          : this.$route.params.certiID,
      imgURL: "../assets/certificate" + this.$route.params.certiID + ".jpg",
      speaker1: "",
      speaker2: "",
      fileName: "",
      emailCheck: false,
    };
  },
  computed: {
    check() {
      return this.steps;
    },
    checkProps() {
      return this.tempID;
    },
  },
  methods: {
    updateStep(num) {
      this.steps = num;
    },
    getImgUrl(imgid) {
      return require("../assets/certificate" + imgid + ".jpg");
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.fileName = files[0].name;
    },
    submit() {
      var bool =
        this.speaker1.length && this.speaker2.length && this.fileName.length;
      if (bool) {
       // alert("Submited Successfuly");
        this.steps = 3;
        axios
          .post("http://127.0.0.1:5000/certificateData", {
            tempID: this.tempID,
            speaker1: this.speaker1,
            speaker2: this.speaker2,
            fileName: this.fileName,
            emailCheck: this.emailCheck,
          })
          .then(function (response) {
            // const data = response.data;
            alert("Success");
          })
          .catch((error) => {
            alert(error);
          });
      } else {
        alert("Some Data Entry is Missing !!");
      }
    },
    email(bools) {
      this.emailCheck = bools;
    },
  },
};
</script>

<style scoped>
.noemail {
  cursor: pointer;
  font-size: 14px;
  padding: 25px;
  padding-top: 10px;
  color: #4a8280;
}
.noemail:hover {
  color: #000;
  font-weight: bolder;
}
.steps {
  width: 40vw;
  height: 88vh;
  background-color: #416d66;
  flex-direction: column;
  font-size: 22px;
  padding-top: 60px;
  padding-bottom: 60px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  color: #0d1413;
  font-weight: bold;
}
.comp {
  width: 60vw;
  height: 88vh;
}
.create-certificate {
  display: flex;
}
.service {
  font-size: 22px;
  color: #4a8280;
  font-style: italic;
  font-weight: bold;
}
.confirm {
  font-size: 20px;
  margin-top: 50px;
}
.contain {
  height: 250px;
  margin: 150px 100px;
  position: relative;
  border: 3px dashed #0d1413;
}
.vertical-center {
  margin: 0;
  position: absolute;
  left: 10%;
  top: 28%;
}
.crumps {
  background-color: #7e9c97;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  border: 2px solid #0d1413;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.active {
  color: #cfcdcd;
}
.show-temp {
  margin: 20px;
}
.confirm:focus {
  outline: none;
}
.head {
  margin: 30px;
  text-align: center;
  font-weight: bold;
  font-size: 20px;
}
.temp {
  margin: 20px;
}
.drop {
  margin-left: auto;
  margin-right: auto;
  width: 25%;
}
.input {
  margin-left: auto;
  margin-right: auto;
  width: 25%;
}
.button {
  margin-left: auto;
  margin-right: auto;
  width: 15%;
}
.certy-btn {
  color: #4a8280;
  padding: 5px 15px;
  border: 1px solid #4a8280;
  background-color: #0d1413;
  border-radius: 32.33px;
  text-decoration: none;
  font-weight: bold;
}
.choose:hover {
  color: #7e9c97;
  cursor: pointer;
}
.certy-btn:hover {
  color: #0d1413;
  border: 1px solid #0d1413;
  background-color: #4a8280;
}
.temp-image {
  width: fit-content;
  height: fit-content;
}
.certi_image {
  height: 70vh;
  display: block;
  border: 2px dashed black;
  margin-left: auto;
  margin-right: auto;
  width: 80%;
}
input {
  margin: 5px 0;
  width: 100%;
  padding: 5px;
  border: 2px solid #0d1413;
}
.show-text {
  margin-top: 40px;
}
</style>