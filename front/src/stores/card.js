import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useCardStore = defineStore('card', () => {
  const cards = ref(null)
  const tempCards = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const brands = [
    "신한카드", "삼성카드", "우리카드", "씨티카드", "KB국민카드", "NH농협카드", 
    "롯데카드", "하나카드", "IBK기업은행", "SC제일은행", "현대카드", "카카오뱅크", 
    "케이뱅크", "우체국", "DGB대구은행", "BNK부산은행", "Sh수협은행", "MG새마을금고", 
    "제주은행", "전북은행"
  ]

  const BRAND_URLS = [
    { brand: '신한카드', url: 'https://www.shinhancard.com/' },
    { brand: '삼성카드', url: 'https://www.samsungcard.com/' },
    { brand: '우리카드', url: 'https://pc.wooricard.com/' },
    { brand: '씨티카드', url: 'https://www.citibank.co.kr/' },
    { brand: 'KB국민카드', url: 'https://card.kbcard.com/' },
    { brand: 'NH농협카드', url: 'https://card.nonghyup.com/' },
    { brand: '롯데카드', url: 'https://www.lottecard.co.kr/' },
    { brand: '하나카드', url: 'https://www.hanacard.co.kr/' },
    { brand: 'IBK기업은행', url: 'https://www.ibk.co.kr/card/mainList.ibk' },
    { brand: 'SC제일은행', url: 'https://www.standardchartered.co.kr/' },
    { brand: '현대카드', url: 'https://www.hyundaicard.com/' },
    { brand: '카카오뱅크', url: 'https://www.kakaobank.com/' },
    { brand: '케이뱅크', url: 'https://www.kbanknow.com/' },
    { brand: '우체국', url: 'https://www.epostbank.go.kr/' },
    { brand: 'DGB대구은행', url: 'https://www.dgb.co.kr/' },
    { brand: 'BNK부산은행', url: 'https://www.busanbank.co.kr/ib20/mnu/FPMCRD122001001' },
    { brand: 'Sh수협은행', url: 'https://suhyup-bank.com/' },
    { brand: 'MG새마을금고', url: 'https://mgcheck.kfcc.co.kr/' },
    { brand: '제주은행', url: 'https://www.e-jejubank.com/' },
    { brand: '전북은행', url: 'https://www.jbbank.co.kr/ '},
    { brand: 'BC 바로카드', url: 'https://paybooc.co.kr/mobile/BCBaroPlus.html?coCd=R005' },
    { brand: 'DB금융투자', url: 'https://dhp.db-fi.com:8100/product/cma/viewProductCmaCardList.dhp' },
    { brand: 'KB증권', url: 'https://m.kbsec.com/go.able?linkcd=et00101' },
    { brand: 'KDB산업은행', url: 'https://smart.kdb.co.kr/mp/MHBMCA01N00.act' },
    { brand: 'KG모빌리언스', url: 'https://www.mobilcard.co.kr/' },
    { brand: 'SBI저축은행', url: 'https://www.sbisb.co.kr/IHPPRODcard0801l.web' },
    { brand: 'SK증권', url: 'http://direct-sks.co.kr/' },
    { brand: 'SSGPAY. CARD', url: 'https://card.ssgpay.com/' },
    { brand: '광주은행', url: 'https://www.kjbank.com/ib20/mnu/FPMCARD010000' },
    { brand: '교보증권', url: 'https://m.iprovest.com/weblogic/CheckCardServlet/checkCard' },
    { brand: '다날', url: 'https://www.danalpay.com/service_introduction/creditcard_payment' },
    { brand: '미래에셋증권', url: 'https://securities.miraeasset.com/' },
    { brand: '신협', url: 'https://openbank.cu.co.kr/' },
    { brand: '아이오로라', url: 'https://www.i-aurora.kr/' },
    { brand: '엔에이치엔페이코', url: 'https://company.payco.com/' },
    { brand: '유진투자증권', url: 'https://www.myasset.com/' },
    { brand: '차이', url: 'https://chai.finance/card/' },
    { brand: '코나카드', url: 'https://www.konacard.co.kr/' },
    { brand: '토스', url: 'https://toss.im/' },
    { brand: '토스뱅크', url: 'https://www.tossbank.com/' },
    { brand: '트래블월렛', url: 'https://www.travel-wallet.com/' },
    { brand: '핀트', url: 'https://www.fint.co.kr/' },
    { brand: '한국투자증권', url: 'https://securities.koreainvestment.com/main/Main.jsp' },
    { brand: '한패스', url: 'https://www.hanpass.com/card' },
    { brand: '현대백화점', url: 'http://www.ehyundai.com/newPortal/card/main.do' }
  ]

  const benefit_dict = ref({
    "간편결제": 0,
    "공과금/렌탈": 1,
    "공항라운지/PP": 2,
    "교육/육아": 3,
    "교통": 4,
    "레저/스포츠": 5,
    "마트/편의점": 6,
    "배달앱": 7,
    "병원/약국": 8,
    "뷰티/피트니스": 9,
    "쇼핑": 10,
    "애완동물": 11,
    "여행/숙박": 12,
    "영화/문화": 13,
    "자동차/하이패스": 14,
    "주유": 15,
    "카페/디저트": 16,
    "통신": 17,
    "푸드": 18,
    "항공마일리지": 19,
    "항공": 20,
    "해외": 21,
  })
  
  const readCard = function () {
    axios({
      method: 'get',
      url: `${API_URL}/cards/`,
    })
    .then(res => {
      cards.value = res.data
      tempCards.value = res.data.slice(0, 40)
    })
    .catch(err => console.error(err))
  }

  const sortCard = function (method) {
    if (method === 'sortName') {
      cards.value.sort((a, b) => a.name.localeCompare(b.name))
    } else if (method === 'sortRecord') {
      cards.value.sort((a, b) => a.record - b.record)
    } else if (method === 'sortAnnualFee') {
      cards.value.sort((a, b) => a.annual_fee1 - b.annual_fee1)
    }
    tempCards.value = cards.value.slice(0, 40)
  }

  const filterCard = (filters) => {
    tempCards.value = cards.value.filter((card) => {
      let matchA = filters.brands.includes(card.brand)

      if (!filters.brands.length) { matchA = true }

      let matchB = false
      if (filters.record < 50) {
        matchB = card.record <= filters.record
      } else {
        matchB = card.record >= filters.record
      }

      let matchC = false
      if (filters.annualFee < 100000) {
        matchC = card.annual_fee1 <= filters.annualFee
      } else {
        matchC = card.annual_fee1 >= filters.annualFee
      }
      return matchA && matchB && matchC
    })
  }

  return {
    cards, tempCards, brands, benefit_dict, API_URL, BRAND_URLS,
    readCard, sortCard, filterCard
  }
}, { persist: true })
